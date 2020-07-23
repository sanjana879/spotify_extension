from gensim import corpora
import pickle
import gensim
NUM_TOPICS = 5

def topic_analyze(tokens):
    del tokens[0][0:3]
    print("topic ", tokens[0][0])
    dictionary = corpora.Dictionary(tokens[0])
    corpus = [dictionary.doc2bow(text) for text in tokens]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')
    topics = ldamodel.print_topics(num_words=4)
    for topic in topics:
        print(topic)
    return