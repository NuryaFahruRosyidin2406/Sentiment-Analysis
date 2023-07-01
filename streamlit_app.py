import nltk
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Dataset
nltk.download('vader_lexicon')

# Title
st.title('Real Time Sentiment Analysis')

# Take a user input
usr_input = st.text_input("Please rate our app: ")

# Process
sentiment = SentimentIntensityAnalyzer()
score = sentiment.polarity_scores(usr_input)

# Condition
if score["neu"] > score["neg"] and score["neu"] > score["pos"]:
    st.write("# Neutral")
elif score["neg"] > score["pos"]:
    st.write("# Negative")
else:
    st.write("# Positive")