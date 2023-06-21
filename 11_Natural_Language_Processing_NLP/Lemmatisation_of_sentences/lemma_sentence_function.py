from nltk.stem import WordNetLemmatizer

import nltk

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas=[]
    for token, pos_tag in zip(sentence_tokens, pos_tags): # looping over sentence_tokens and the pos_tags.
        if pos_tag[1][0].lower() in ['n', 'v', 'a','r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    return sentence_lemmas

l1 = lemma_me('Vegetables are types of plants')
print(l1)

l2 = lemma_me('A vegetable is a type of plant')
print(l2)

print(l1 == l2)  #True!