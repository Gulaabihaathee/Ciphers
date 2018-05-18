import numpy as np
from textwrap import wrap

#5-letter 
key_word = 'LIGHT'
phrase_to_code = 'TIMES OF DARKNESS'

def encode_pf(key_word, phrase_to_code): 
    alfabet =  [chr(i) for i in range(65,65+26)]
    alfabet[alfabet.index('I'):alfabet.index('J')+1] = ['/'.join(alfabet[alfabet.index('I'):alfabet.index('J')+1])]

    if('I' in key_word or 'J' in key_word):
        alfabet.remove('I/J')
    alfabet = sorted(set(alfabet) - set(list(key_word)))

    array = np.asanyarray(list(key_word) + alfabet).reshape(5,5)
    phrase_to_code = phrase_to_code.replace(' ', '')

    for i in range(0,len(phrase_to_code)-1,2):
            if(phrase_to_code[i] == phrase_to_code[i+1]):
                    phrase_to_code = phrase_to_code[:i+1] + 'X' + phrase_to_code[i+1:]

    if (len(phrase_to_code) %2 != 0):
        phrase_to_code+='X'

    phrase_twos = wrap(phrase_to_code, 2)
    coded_word = []

    for digram in phrase_twos:
        first_letter_loc = (np.where(array==digram[0])[0][0],np.where(array==digram[0])[1][0])
        second_letter_loc = (np.where(array==digram[1])[0][0],np.where(array==digram[1])[1][0])

        #LETTERS IN THE SAME ROW
        if(first_letter_loc[0] == second_letter_loc[0]):
            if (first_letter_loc[1] == 4):
                new_first_letter = (first_letter_loc[0], 0)
            if (second_letter_loc[1] == 4):
                new_second_letter = (second_letter_loc[0], 0)
            if (first_letter_loc[1] < 4):
                new_first_letter = (first_letter_loc[0], first_letter_loc[1]+1)
            if (second_letter_loc[1] < 4):
                new_second_letter = (second_letter_loc[0], second_letter_loc[1]+1)
        
        #LETTERS IN THE SAME COLUMN
        if(first_letter_loc[1] == second_letter_loc[1]):
            if (first_letter_loc[0] == 4):
                new_first_letter = (0, first_letter_loc[1])
            if (second_letter_loc[0] == 4):
                new_second_letter = (0, second_letter_loc[1])
            if (first_letter_loc[0] < 4):
                new_first_letter = (first_letter_loc[0]+1, first_letter_loc[1])
            if (second_letter_loc[0] < 4):
                new_second_letter = (second_letter_loc[0]+1, second_letter_loc[1])

        if(first_letter_loc[0] != second_letter_loc[0] and first_letter_loc[1] != second_letter_loc[1]):
            new_first_letter = (first_letter_loc[0], second_letter_loc[1])
            new_second_letter = (second_letter_loc[0], first_letter_loc[1])

        coded_word.append(array[new_first_letter] + array[new_second_letter])

    return(coded_word)
