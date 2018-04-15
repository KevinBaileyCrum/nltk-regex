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

    pattern = re.compile(r'(?P<NP>(?:\S+/DT\s*)?(?:\S+/JJ\w?\s*)*(?:\S+/NN\w*\s*)+)')
    matches = re.findall( pattern, pos_sent ) # match patter in regex

    # init list of phrases and use get_words to strip off POS tag
    phrase_list = []
    for words in matches:
        print( words )
        phrase_list.append( get_words( words ) )
    print( phrase_list )
    return matches

def most_freq_noun_phrase(pos_sent_fname):
    # Your code goes here
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

    pythexab = """ word/thing boo/thang this/DT hot/JJ real/JJR School/NN \
    Magnolias/NNPS a/JJ a/JJR b/JJS c/NN d/NNS f/NNP z/NNPS """
    print(pos_sent)
    # print(str(get_words(pos_sent)))
    # print(str(get_noun_phrase(pos_sent)))
    print("############################################################")
    print(str(get_noun_phrase(pos_sent)))
    print("##############################################################")
    print(pythexab)
    print(str(get_noun_phrase(pythexab)))

    most_freq_noun_phrase(pos_sent_fname)

