from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas=[]
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a','r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    return sentence_lemmas

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked'
question = 'What are vegetables?'

sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
print(sentence_tokens)

#<python path> -m pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

tv = TfidfVectorizer(tokenizer=lemma_me)

#print(tv) #--> TfidfVectorizer(tokenizer=<function lemma_me at 0x7fea5d0d99d0>)

#nltk.download('averaged_perceptron_tagger')

tf = tv.fit_transform(sentence_tokens)
#print(tf.toarray())

import pandas
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())
print(df)

from sklearn.metrics.pairwise import cosine_similarity
values = cosine_similarity(tf[-1], tf)

"""
# Note: tf is:
         be   collect      cook       eat  hunter-gatherer  originally     plant  vegetable
0  0.277174  0.531146  0.000000  0.000000         0.531146    0.531146  0.000000   0.277174
1  0.419880  0.000000  0.000000  0.000000         0.000000    0.000000  0.804612   0.419880
2  0.327134  0.000000  0.626884  0.626884         0.000000    0.000000  0.000000   0.327134
3  0.707107  0.000000  0.000000  0.000000         0.000000    0.000000  0.000000   0.707107     <---- tf[-1](question)
"""

print(values) # --> [[0.39198343 0.59380024 0.46263733 1.        ]]
"""
here 0.39198343 is similarity between question and first sentence and so on"""


index = values.argsort()
print(index) # --> array inside list [[0 2 1 3]] Here 0 is first element from values, 2 is third element and so on in increasing order

index = values.argsort()[0][-2] # -2 since we want the second highest since first highest that matches would be at -1 and that we know is the question itself!
print(index) #--> 1

values_flat = values.flatten()
print(values_flat) # we get just one list instead of the nested structure

values_flat.sort()
print(values_flat)

coeff = values_flat[-2] # #last but one item
print(coeff)

if coeff > 0.3:
    print(sentence_tokens[index])