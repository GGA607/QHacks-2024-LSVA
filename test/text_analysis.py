"""
QHacks 2024 Project

TODO: This file is meant to interpret the transcribed user text file and return a rating based on the provided input.

Authors: Alec Glasford, Logan Jarvis, Shravan Agnihotri, Vedansh Bhatt
Last Modified: 2024/02/03
"""
#importing our librarys
import pandas as pd
import nltk
#importing specfic functions from out librarys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


#creating our functions to manage our data

def data_preperation(text):
    # Tokenizing the text
    tokens = word_tokenize(text.lower())

    # Removing stop words with nltk's built-in model
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize the tokens to reduce words to their base form
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    # Rejoin the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

# create get_sentiment function
def get_sentiment(text):
    # initialize NLTK sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    #  rating the overall text
    ratings = analyzer.polarity_scores(text)
    sentiment = 1 if ratings['pos'] > 0 else 0

    return sentiment

def get_analysis(text):
    return get_sentiment(data_preperation(text))