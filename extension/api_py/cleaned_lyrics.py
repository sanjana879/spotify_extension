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
    replaced = [[]]
    words = [[]]
    for song in lyrics:
        song = re.sub(r'[\(\[].*?[\)\]]', '', str(song))
        song = song.replace('\n', ' ')
        song = os.linesep.join([s for s in song.splitlines() if s])
        words.append(song.split(" "))
        replaced.append(song)

    filtered_words = [[]]
    for song in words:
        filtered_words.append([word for word in song if
                      word not in stopwords.words('english') and len(word) > 1 and word not in ['na', 'la', 'oh', 'baby']])

    filtered_all_words = []
    for song in filtered_words:
        song_lyrics = ''
        for word in song:
            song_lyrics += word + ' '
        filtered_all_words.append(song_lyrics)
    for song in filtered_all_words:
        song = os.linesep.join([s for s in song.splitlines() if s])

    return filtered_all_words

def tokenize(lyrics):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    tokens = [[]]
    for song in lyrics:
        print("token ", len(song))
        song = song.translate(translate_table)
        tokens.append(word_tokenize(song))
    #print(tokens)
    result = lemmatize_stemming(lyrics)
    return tokens, result

def lemmatize_stemming(text):
    nltk.download('wordnet')
    stemmer = PorterStemmer()
    result=[[]]
    #text = all_words
    for song in text:
        song_ly = []
        for token in gensim.utils.simple_preprocess(song) :
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
                #print(token, '\n')
                song_ly.append(stemmer.stem(WordNetLemmatizer().lemmatize(token, pos='v')))
        result.append(song_ly)
    #print(result)
    return result