def encode_bc(docu, WORD):
    from random import choice
    doc = open(docu, 'r' )
    
    data = []
    for line in doc.readlines():
            data.append(line.lower().split())

    data = list(filter(None, data))

    WORD = WORD.lower() 
    WORD = list(WORD)
    coded_string = []

    for word_letter in WORD:
        possibilities = []
        for i_line, line in enumerate(data):
                for i_word, word in enumerate(line):
                        for i_letter, letter in enumerate(word):
                                if(word_letter == letter):
                                        possibilities.append([i_line+1, i_word+1, i_letter+1])
        coded_string.append(choice(possibilities))
 

    return(coded_string)

def decode_bc(docu, coded_string):
    doc = open(docu, 'r' )
    data = []
    for line in doc.readlines():
            data.append(line.lower().split())

    data = list(filter(None, data))
    word = ''
    for coded_letter in coded_string:
        word += data[coded_letter[0]-1][coded_letter[1]-1][coded_letter[2]-1]
    return(word)

print(decode_bc('DOC.txt', encode_bc('DOC.txt', 'Gonitwa')))
