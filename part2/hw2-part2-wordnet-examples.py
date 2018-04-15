from nltk.corpus import wordnet as wn

# http://stevenloria.com/tutorial-wordnet-textblob/
# http://www.nltk.org/howto/wordnet.html
# http://wordnetweb.princeton.edu/perl/webwn

def print_syn_lemmas(word):

    ## Synsets and Lemmas
    f.write("1. Synsets and Lemmas")
    f.write("Word: " + word)
    f.write("")
    f.write("Synsets:")
    [f.write(s) for s in wn.synsets(word)]
    f.write("")
    first_synset = wn.synsets(word)[0]
    f.write("First synset: " + str(first_synset))
    f.write("")

    #word_synset = wn.synset("dog.n.01")
    f.write("Lemma names: ")
    [f.write(l) for l in first_synset.lemma_names()]
    f.write("")
    last_lemma = first_synset.lemmas()[len(first_synset.lemma_names())-1]
    #word_lemma = wn.lemma("dog.n.01.domestic_dog")
    f.write("Last lemmas: " + str(last_lemma))
    f.write("")
    f.write("Synset of Last lemmas: " + str(last_lemma.synset()))
    f.write("")
    for synset in wn.synsets(word):
        f.write(str(synset) + ": lemma_name" + str(synset.lemma_names()))
    f.write("")
    f.write("Lemmas of {}:".format(word))
    [f.write(l) for l in wn.lemmas(word)]
    f.write("")
    f.write("")

def print_def_exp(synset):
    ## Definitions and Examples
    f.write("2. Definitions and Examples")
    f.write("Synset: " + str(synset))
    f.write("Definition: " + synset.definition())
    f.write("")
    f.write("Example: " + str(synset.examples()))
    f.write("")
    f.write("Synsets of first lemma " + str(synset.lemma_names()[0]) + ": ")
    for synset in wn.synsets(synset.lemma_names()[0]):
        f.write(synset, ": definition (", synset.definition() + ")")
    f.write("")
    f.write("")

def print_lexical_rel(synset):
    ## Lexical Relations
    f.write("3. Lexical Relations")
    f.write("Synset: " + str(synset))
    f.write("")
    f.write("Hypernyms: " + str(synset.hypernyms()))
    f.write("")
    f.write("Hyponyms: " + str(synset.hyponyms()))
    f.write("")
    f.write("Root hypernyms: " + str(synset.root_hypernyms()))
    f.write("")

    paths = synset.hypernym_paths()
    f.write("Hypernym path length of {} = {} ".format(str(synset), str(len(paths))))
    f.write("")
    for i in range(len(paths)):
        f.write("Path[{}]:".format(i))
        [f.write(syn.name()) for syn in paths[i]]
        f.write("")
    f.write("")

def print_other_lexical_rel():
    good1 = wn.synset('good.a.01')
    wn.lemmas('good')
    f.write("Antonyms of 'good': " + str(good1.lemmas()[0].antonyms()))
    f.write("")
    f.write("Entailment of 'walk': " + str(wn.synset('walk.v.01').entailments()))
    f.write("")

if __name__ == '__main__':
    f= open("part2.out","w+")
    #f.write_syn_lemmas('set')
    #f.write_def_exp(wn.synset("set.n.01"))
    #f.write_lexical_rel(wn.synset("set.n.01"))
    #f.write_other_lexical_rel()

    print_syn_lemmas('set')
    print_def_exp(wn.synset("set.n.01"))
    print_lexical_rel(wn.synset("set.n.01"))
    print_other_lexical_rel()

