"""
QHacks 2024 Project

TODO: This file is meant to interpret the transcribed user text file and return a rating based on the provided input.

Authors: Alec Glasford, Logan Jarvis, Shravan Agnihotri, Vedansh Bhatt
Last Modified: 2024/02/03
"""
#importing our librarys
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

    # get the compound score
    compound_score = analyzer.polarity_scores(text)['compound']
    print(text + "- score on a scale from [-1, 1] for positivity.")
    # 1 for positive sentiment if the compound score is greater than or equal to 0

    return compound_score

def get_analysis(text):
    return get_sentiment(data_preperation(text))

if __name__ == "__main__":
    print("I love QHacks 2024!")
    print(get_analysis("I love QHacks 2024!"))