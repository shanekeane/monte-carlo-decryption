import numpy as np
import copy

def create_init_mapping(seq, symbols, symb_count):
    #Outputs an initial guess of the decryption mapping
    seq_count = np.char.count(seq, symbols) #count of each symbol in seq
    sorted_inds_normal = np.argsort(symb_count)
    sorted_normal = symbols[sorted_inds_normal]
    sorted_inds_enc = np.argsort(seq_count)
    sorted_encrypted = symbols[sorted_inds_enc]
    mapping = dict()
    for crypt, symbol in zip(sorted_encrypted, sorted_normal):
        mapping[crypt] = symbol
        
    return mapping

def remap(mapping):
    #Permutes two elements
    #Takes and returns a dictionary
    out_map = copy.deepcopy(mapping)
    inds = np.random.choice(list(out_map.keys()),\
                            2, replace = False)
    temp = out_map[inds[0]]
    out_map[inds[0]]= out_map[inds[1]]
    out_map[inds[1]] = temp

    return out_map

def decrypt(sequence, mapping):
    #Take string sequence and outputs decrypted string
    decrypted_string = ""
    for letter in sequence:
        decrypted_string += mapping[letter]
        
    return decrypted_string

def get_pair_prob(pair, pair_array, log_t_mat):
    inds = np.where(pair_array == pair)
    return log_t_mat[inds[0][0], inds[1][0]]

def get_init_prob(symbol, symbols, log_stat):
    ind = np.where(symbols == symbol)
    return log_stat[ind[0][0]]

def get_seq_prob(sequence, p_array, log_tmat, symbols, log_stat):
    #Returns log-probability 
    total_prob = 0.0
    #Initial state
    total_prob += get_init_prob(sequence[0], symbols, log_stat)
    counts = np.char.count(sequence, p_array)
    char_probs = log_tmat * counts 
    total_prob += np.sum(char_probs)
    return total_prob  

def get_encrypt_prob(sequence, mapping, p_array, log_tmat, symbols, log_stat):
    #Get probability of encrypted sequence
    #First decrypt and then get prob
    decrypted_seq = decrypt(sequence, mapping)
    return get_seq_prob(decrypted_seq, p_array, log_tmat, symbols, log_stat)

def mh(sequence, init_mapping, p_array, log_tmat, symbols, log_stat):
    #Metropolis-Hastings algorithm
    current_map = init_mapping
    log_p_old = get_encrypt_prob(sequence, current_map, p_array, log_tmat,\
                                 symbols, log_stat)
    count = 0
    #Values to be used for convergence testing
    best = 0
    best_prob = log_p_old
    #
    first_chars = list()
    first_chars.append(decrypt(sequence, current_map)[:60])
    
    while True:
        count += 1
        proposal = remap(current_map)
        log_p_new = get_encrypt_prob(sequence, proposal, p_array,\
                                     log_tmat, symbols, log_stat)
        
        #Get A in log space
        A = min(0.0, (log_p_new - log_p_old))
        if np.log(np.random.uniform()) < A:
            current_map = proposal
            log_p_old = log_p_new
            
            #Establishing conditions
            if log_p_new > best_prob:
                best_prob = log_p_new
                best_out = decrypt(sequence, current_map)
                best = 0
            else:
                if np.abs(log_p_new - best_prob) < 1e-10:
                    best += 1


        if count % 100 == 0:
            first_chars.append(decrypt(sequence, current_map)[:60])
            prob_curr = log_p_old
            print(f"Iters: {count}")
            print(decrypt(sequence, current_map) + '\n')
            
        #Best counts how many times jumps are rejected because
        #the present location is the best
        if best > 300:
            break
            
    return first_chars, count, best_out
