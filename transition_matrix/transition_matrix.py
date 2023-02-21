import numpy as np

def get_symbol_pairs(symbs):
    #Output an array of all symbol pairs - e.g. ab, cd etc.
    pairs_array = np.empty([len(symbs), len(symbs)],\
                           dtype = object)
    for i in range(len(symbs)):
        for j in range(len(symbs)):
            pairs_array[i,j] = symbs[i] + symbs[j]
    return pairs_array

def get_trans_matrix(file_name, symbols):
    #Takes file for generating transition matrix - e.g. War and Peace
    #Takes list of all symbols in our dictionary

    symbol_count = np.zeros(len(symbols), dtype = 'int') #for counting symbols
    
    #Generate matrix of symbol pairs
    symbol_pairs = get_symbol_pairs(symbols)
    
    #Initiate transition matrix to ones, as some symbols 
    #may not appear
    t_mat = np.ones_like(symbol_pairs)
    
    #Open file and read in lines
    f1 = open(file_name, 'r')
    lines = f1.readlines()
    for line in lines:
        #Some character replacements necessary due
        #to formatting of the file
        line = line.replace('\n', ' ').lower()
        line = line.replace('“','"')
        line = line.replace('”','"')
        line = line.replace('’',"'")
        #For each line, record instances of pairs
        for i in range(len(line) - 1):
            pair = line[i:i+2]
            if pair in symbol_pairs:
                p_inds = np.where(symbol_pairs == pair)
                t_mat[p_inds[0][0], p_inds[1][0]] += 1.0
        #For each line, record number of each symbol
        for i in range(len(line)):
            sym = line[i]
            if sym in symbols:
                s_ind = np.where(symbols == sym)
                symbol_count[s_ind[0][0]] += 1
                
    #Divide by row total for transition matrix
    row_sum = np.sum(t_mat, axis = 1)
    t_mat = (t_mat.T/row_sum).T
    return t_mat, symbol_count
