import re, nltk

def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))

def get_text(review):
    return re.search(r'Text = "(.*)"', review).group(1)

def write_freqDist( category, file_name ):
    # creates a file 'positve | negative'.txt
    # writes most common words in descending order to file
    filename = category+'.txt'
    f = open( filename, "w+" )
    fdist = nltk.FreqDist( normalize( file_name ) )
    f.write( str( fdist.most_common() ) )
    f.close()
    pass

def normalize( file_name ):
    # normalize data set to yield more useful data
    # current implementation is ineffecient as it
    # iterates through the same list multiple times
    # could be improved for larger data sets

    # lowercase all tokens
    words = [ w.lower() for w in file_name ]

    # remove stopwords
    stop_words = set( nltk.corpus.stopwords.words( 'english' ) )
    words = [ w for w in words if not w in stop_words ]

    # remove tokens w/o 1+ \w
    regex = re.compile(r'(?:\w)+')
    normalized_words = []
    for w in words:
        normalized_words += ( re.findall( regex, w ) )

    return ( normalized_words )

def process_reviews(file_name):
    file = open(file_name, "rb")
    raw_data = file.read().decode("latin1")
    file.close()

    positive_texts = []
    negative_texts = []
    first_sent = None
    for review in re.split(r'\.\n', raw_data): # parse reviews separated by .
        overall_score = get_score(review)
        review_text = get_text(review)
        if overall_score > 3:
            positive_texts.append(review_text)
        elif overall_score < 3:
            negative_texts.append(review_text)
        if first_sent == None:
            sent = nltk.sent_tokenize(review_text)
            if (len(sent) > 0):
                first_sent = sent[0]

    # There are 150 positive reviews and 150 negative reviews.
    # print(len(positive_texts))
    # print(len(negative_texts))
    # Your code goes here
    write_freqDist( 'positive', positive_texts )
    write_freqDist( 'negative', negative_texts )
    #normalize( negative_texts )
    #print( positive_texts )

# Write to File, this function is just for reference, because the encoding matters.
def write_file(file_name, data):
    file = open(file_name, 'w', encoding="utf-8")    # or you can say encoding="latin1"
    file.write(data)
    file.close()

if __name__ == '__main__':
    #filename = sys.argv[1]
    file_name = "restaurant-training.data"
    process_reviews(file_name)
