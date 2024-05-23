import nltk

with open("miracle_in_the_andes.txt", "r", encoding="UTF-8") as file:
    book = file.read()

import re
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
findings[:5]

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
d_list[:5]

from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

filtered_words[:10]


### Sentiment Analysis: What is the most positive and most negative chapter

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

scores = analyzer.polarity_scores(text="I hate you")

if scores["pos"] > scores['neg']:
    print("It is a positive text")
else:
    print("It is a negative text")


### Chapter sentiment analysis
import re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)

chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(text=chapter)
    print(scores)