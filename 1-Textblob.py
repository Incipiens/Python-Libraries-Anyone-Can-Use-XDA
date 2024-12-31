from textblob import TextBlob

blob = TextBlob("We love XDA!")
print(blob.correct())
print(blob.sentiment)