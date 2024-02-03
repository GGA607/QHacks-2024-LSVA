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

