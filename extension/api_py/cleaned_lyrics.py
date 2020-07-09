import re
import os
import string

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import *
import gensim
import gensim.corpora as corpora

def clean_lyrics(lyrics):
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', str(lyrics))
    lyrics = lyrics.replace('\\n', ' ')
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
    words = lyrics.split(" ")
    filtered_words = [word for word in words if
                      word not in stopwords.words('english') and len(word) > 1 and word not in ['na', 'la', 'oh',
                                                                                                'baby']]
    filtered_all_words = ''
    for word in filtered_words:
        filtered_all_words += word + ' '
    filtered_all_words = os.linesep.join([s for s in filtered_all_words.splitlines() if s])
    return filtered_all_words

def tokenize(lyrics):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    lyrics = lyrics.translate(translate_table)
    tokens = word_tokenize(lyrics)
    print(tokens)
    result = lemmatize_stemming(lyrics)
    return tokens, result

def lemmatize_stemming(text):
    nltk.download('wordnet')
    stemmer = PorterStemmer()
    result=[]
    #text = all_words
    for token in gensim.utils.simple_preprocess(text) :
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            #print(token, '\n')
            result.append(stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v')))
    print(result)
    return result