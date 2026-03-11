import pandas as pd
from textblob import TextBlob

data = pd.read_excel("customer_reviews.xlsx")

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

data["Sentiment"] = data["ReviewText"].apply(get_sentiment)

data.to_excel("reviews_with_sentiment.xlsx", index=False)

print(data.head())
