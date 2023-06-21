import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#nltk.download('vader_lexicon')
#nltk.download('twitter_samples')

analyzer = SentimentIntensityAnalyzer()

text1 = 'Hey, what a beautiful day! How amazing it is!'
print(f"Polarity scores are: {analyzer.polarity_scores(text1)}")
#{'neg': 0.0, 'neu': 0.42, 'pos': 0.58, 'compound': 0.8513}
# pos - positivity, neu - neutrality, pos - positivity . always : neg+neu+pos = 1
# compound - ranges from -1 to 1 - closer it is to 1, the more positive it is!

if analyzer.polarity_scores(text1)['compound'] > 0:
    print('Positive Text')
else:
    print('Negative Text')

print(len(nltk.corpus.twitter_samples.strings()))

tweet1 = nltk.corpus.twitter_samples.strings()[44]
print(tweet1)

print(analyzer.polarity_scores(tweet1))