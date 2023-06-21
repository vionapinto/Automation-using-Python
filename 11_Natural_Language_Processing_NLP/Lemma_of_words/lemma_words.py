from nltk.stem import WordNetLemmatizer
import nltk
x = 'was'
y = 'is'


# nltk --> Natural Language Tool Kit

lemmatizer = WordNetLemmatizer()

# Root is known as the lemma of the word

#nltk.download('wordnet') # we need to download the dictionary first!

lemma1 = lemmatizer.lemmatize(x, 'v')
# "v" for verbs, "a" for adjectives, "r" for adverbs and "s" for satellite adjectives, "n" is default

lemma2 = lemmatizer.lemmatize(y,'v')

print(lemma1)
print(lemma2)

print(lemma1 == lemma2)


## Also, lets try with noun and plurals:

lemma3 = lemmatizer.lemmatize('vegetable','n')
lemma4 = lemmatizer.lemmatize('vegetables','n')

print(lemma3)
print(lemma4)  #--> Output: vegetable!!!

print(lemma3 == lemma4)