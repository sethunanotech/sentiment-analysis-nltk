import nltk;

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer;

def analysis_sentiment(text):
    sid = SentimentIntensityAnalyzer();
    sentiment_score = sid.polarity_scores(text);
    return sentiment_score;

text = "The people are happy for this grocery price hike";
sentiment_score = analysis_sentiment(text);
print(sentiment_score);