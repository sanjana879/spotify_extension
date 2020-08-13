import matplotlib.pyplot as plt
import numpy as np
from nrclex import NRCLex
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
plt.rcdefaults()


def sentiment_analysis(lyrics):
    sid = SentimentIntensityAnalyzer()
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    for sentence in lyrics:
        #this_sentence = sentence.decode('utf-8')
        comp = sid.polarity_scores(sentence)
        comp = comp['compound']
        if comp >= 0.5:
            num_positive += 1
        elif -0.5 < comp < 0.5:
            num_neutral += 1
        else:
            num_negative += 1

    num_total = num_negative + num_neutral + num_positive
    percent_negative = (num_negative / float(num_total)) * 100
    percent_neutral = (num_neutral / float(num_total)) * 100
    percent_positive = (num_positive / float(num_total)) * 100
    print(percent_negative, percent_neutral, percent_positive)
    percents = [percent_negative, percent_neutral, percent_positive]
    titles = ["Negative", "Neutral", "Positive"]
    return zip(titles, percents)


def detailed_emotions(lyrics):
    text_lyrics = ' '
    text_lyrics = text_lyrics.join(lyrics)
    text_object = NRCLex(text_lyrics)
    scores = text_object.raw_emotion_scores
    freq = text_object.affect_frequencies
    print(text_object.affect_dict)
    print(len(lyrics[0]))
    print(len(lyrics[1]))
    print(len(lyrics[2]))
    print(freq)
    # 'anticip': 1471, 'positive': 1671, 'negative': 1622, 'sadness': 1496, 'disgust': 1507, 'joy': 1520, 'anger': 1481, 'surprise': 1385, 'fear': 1532, 'trust':
    emotions = ('anticipation', 'positive', 'negative', 'sadness',
                'disgust', 'joy', 'anger', 'surprise', 'fear', 'trust')
    return (scores)
