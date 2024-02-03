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

#initializaing our dataframe
df = pd.read_csv("dummy_data.csv")

#initializaing our text string from the answer.txt file
text = ''
with open("answer.txt", "r") as f:
    for i in f:
        text = f.read()

#creating our functions to manage our data
def data_preperation(text):
    #tokenizing the text
    tokens = word_tokenize(text.lower)
    
    #removing stop words with nltk's built in model
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    #lemmatize the tokens. this reduces words into their base form and allow for a more simple understanding
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    #rejoins the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

# adding "reviewText" by calling the data_preperation method to clean the data of stopping words, then lemmatizing them
df['reviewText'] = df['reviewText'].apply(data_preperation)

# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# create get_sentiment function
def get_sentiment(text):

    #  rating the overall text
    ratings = analyzer.polarity_scores(text)
    sentiment = 1 if ratings['pos'] > 0 else 0

    return sentiment


# adding "sentiment" by calling the get_sentiment method to evaluate the polarity of the text
df['sentiment'] = df['reviewText'].apply(get_sentiment)

print(df.head)