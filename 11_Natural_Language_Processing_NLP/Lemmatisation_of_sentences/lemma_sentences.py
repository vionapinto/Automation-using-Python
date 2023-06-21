from nltk.stem import WordNetLemmatizer

import nltk

lemmatizer = WordNetLemmatizer()
sentence = 'Vegetables are types of plants.'
"""lemma1 = lemmatizer.lemmatize('Vegetables are types of plants','n')

print(lemma1) # out: Vegetables are types of plants"""

# This isn't the output we want. We want it to be lemmatized.
# So we will try breaking the sentence into words and lemmatizing them.
# This process is called Tokenizing the sentence

# TOKENIZING SENTENCES
# You need to download the punkt dictionary. One Time!
# nltk.download('punkt')

sentence_tokens = nltk.word_tokenize(sentence.lower())
# we use lower() here because we need to pass these words through lemmatizer and lemmatize function works on lower case only!
print(sentence_tokens)

nltk.download('averaged_perceptron_tagger')

pos_tags = nltk.pos_tag(sentence_tokens)
print(pos_tags)

""" for token in sentence_tokens:
    lemma = lemmatizer.lemmatize(token, 'n')
    print(lemma)
    # If we use 'n' it lemmatizes nouns but not verb are to be.
    # if we use 'v' it lemmatizes verb but remains vegetables.
    # Hence we need pos tags for each of the tokens. (POS - Part Of Speech) """

sentence_lemmas=[]
for token, pos_tag in zip(sentence_tokens, pos_tags): # looping over sentence_tokens and the pos_tags.
    if pos_tag[1][0].lower() in ['n', 'v', 'a','r']:
        lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())  # pos_tag = ('vegetables', 'NNS')-- we want the first N. Hence [1] gives 2nd element of tuple ie NNS and [0] gives us N. It should be in lower case for the lemmatizer.
        # This will give and error since ('of', 'IN') doesn't have a lemma. Hence we need a if loop here!
        sentence_lemmas.append(lemma)

print(sentence_lemmas)


# In the next file we write it neatly inside a function!