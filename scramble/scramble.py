import numpy as np
import os
PATH = os.getcwd()
DATA_PATH = os.path.abspath(os.path.join(PATH, os.pardir)) + '/data'

def scramble(text_file, symbols, output_file_name=None, outp=True):    
    """
    Scrambles a text given in text file
    
    Inputs: text_file        : input text
            symbols          : list of valid symbols
            output_file_path : where to save the scrambled text
            outp             : whether to print scrambled text
    """
    #Create cipher dictionary
    inds = np.arange(len(symbols))
    np.random.shuffle(inds)
    cipher_dict = {symbols[i]: symbols[inds][i] for i in range(len(symbols))}

    #Import text and turn into array
    with open(text_file, 'r') as f:
        text = f.read().strip().lower()
    text_chars = np.asarray(list(text))

    #Error check
    try: 
        assert(False not in np.in1d(text_chars, symbols))
    except AssertionError as err:
        wrong_char_inds = np.asarray([False  if i else True for i in np.in1d(text_chars, symbols)])
        print('Invalid character(s) in input file:')
        print(text_chars[wrong_char_inds])
        exit()
        
    cipher_text = "".join([cipher_dict[i] for i in text_chars])
    
    if outp == True:
        print(cipher_text)
        
    if output_file_name is None:
        exit()
    else:
        with open(output_file_name, "w") as f_out:
            f_out.write(cipher_text)
