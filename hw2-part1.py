import argparse, re, nltk

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://www.debuggex.com/

def get_words(pos_sent):
    # Your code goes here
    pass

def get_noun_phrase(pos_sent):
    # Penn Tagset
    # Adjetive can be JJ,JJR,JJS
    # Noun can be NN,NNS,NNP,NNPS

    # Your code goes here
    pass

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
    print(pos_sent)
    print(str(get_words(pos_sent)))
    print(str(get_noun_phrase(pos_sent)))

    most_freq_noun_phrase(pos_sent_fname)

