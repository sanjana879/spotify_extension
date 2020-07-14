import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


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
    return percent_negative, percent_neutral, percent_positive