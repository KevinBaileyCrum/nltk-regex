# Fri Apr 13 11:06:09 PDT 2018
import argparse, re, nltk

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://www.debuggex.com/

def get_words(pos_sent):
    reg_str = r"([\.A-z]+)(?=\/)"
    matches = re.findall(reg_str, pos_sent)
    return matches

def get_noun_phrase(pos_sent):
    # Matches noun_phrase(s) using the Penn Tagset
    # Adjetive can be JJ,JJR,JJS
    # Noun can be NN,NNS,NNP,NNPS
    # ADJC = r"([A-z]+([/])(JJS|JJR|JJ)"
    # NOUN = r"(NNPS|NNS|NNP|NN)"
    # DETR = r"([A-z]+/DT)"
    # Parses phrase. calls get_words to return tokens as words

    # regex = r"(([A-z]+\/DT)? ([A-z]+\/((JJS)|(JJR)|(JJ)))+ ([A-z]+\/((NNPS)|(NNS)|(NNP)|(NN)))*)"

    regex = re.compile(r'((?:\S+/DT\s*)?(?:\S+/JJ\w?\s*)*(?:\S+/NN\w*\s*)+)')

    # regex = re.compile(r'(?:[ A-z]+/DT
    matches = re.findall( regex, pos_sent ) # match patter in regex

    # init list of phrases and use get_words to strip off POS tag
    phrase_list = []
    for words in matches:
        phrase_list.append( get_words( words ) )
    # combine sublists in phrase_list ( formatting output )
    phrase_list = [' '.join(words) for words in phrase_list]
    return phrase_list

def most_freq_noun_phrase(pos_sent_fname):
    # open file
    print(pos_sent_fname)
    f= open(pos_sent_fname,"r")
    print( str( get_noun_phrase( f ) ) )
    pass

if __name__ == '__main__':

    # python hw2-part1-stub.py -f fables-pos.txt
    # python hw2-part1-stub.py -f blogs-pos.txt
    parser = argparse.ArgumentParser(description='Assignment 2')
    parser.add_argument('-f', dest="pos_sent_fname",
                              default="fables-pos.txt",
                              help='File name that contant the POS.'
                       )

    args = parser.parse_args()
    pos_sent_fname = args.pos_sent_fname

    pos_sent = """All/DT animals/NNS are/VBP equal/JJ ,/, but/CC some/DT \
    animals/NNS are/VBP more/RBR equal/JJ than/IN others/NNS ./."""
    print()
    print(pos_sent)
    print()
    print('1: -------------------------------------------------------')
    print(str(get_words(pos_sent)))
    print('   -------------------------------------------------------')

    print('2: -------------------------------------------------------')
    print(str(get_noun_phrase(pos_sent)))
    print('   -------------------------------------------------------')


    print('3: -------------------------------------------------------')
    most_freq_noun_phrase(pos_sent_fname)
    print('   -------------------------------------------------------')
