import nltk
from nltk.corpus import stopwords
import string


def analyze_general(soup):
    """
    This is meant to analyze a web page in a generic manner (not site-specific)
    Get title
    Get text
        - Manipulate
        - Determine topic
            - Determine keywords
        - Determine how it presents the information
            - article
            - forum
        - Determine if it is a question and whether there is an answer
        - Determine whether the information may be stored in a special manner that makes
          it more difficult to analyze (table, image, etc)
            - Maybe should add image-to-text recognition in order to analyze information
              in such cases
            - use pandas for table analysis
    Save
    :param soup:
    :return:
    """

    # Preprocess
    text = soup.get_text()

    text = text.translate(str.maketrans(dict.fromkeys(string.punctuation)))

    tokens = nltk.word_tokenize(text)

    print(tokens)

    # Removing stop words
    for token in tokens:
        if token in stopwords.words('english'):
            tokens.remove(token)

    # Getting max frequency word
    freq = nltk.FreqDist(tokens)

    for key, val in freq.items():
        print(str(key) + ':' + str(val))
    freq.plot(20, cumulative=False)

    # Part of speech tagging
    tokens = nltk.pos_tag(tokens)

    print(tokens)

    # pattern = 'NP: {<DT>?<JJ>*<NN>}'
    # cp = nltk.RegexpParser(pattern)
    # cs = cp.parse(tokens)
    # print(cs)
