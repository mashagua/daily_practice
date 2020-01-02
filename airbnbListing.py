from pprint import pprint
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import spacy
import scattertext as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
plt.style.use("seaborn")
warnings.filterwarnings(action='ignore')
listing = pd.read_csv('data/listings.csv')
listing['review_scores_ratings'] = listing['review_scores_rating'] / 20
listing['review_scores_ratings'] = pd.cut(
    listing['review_scores_ratings'], bins=5, labels=[
        "0.0-1.0", "1.0-2.0", "2.0-3.0", "3.0-4.0", "4.0-5.0"])
listing['description'].replace(np.NaN, "no_description", inplace=True)
listing["review_scores_ratings"].replace(np.NaN, "no_review", inplace=True)
nlp = spacy.load("en")
corpus = st.CorpusFromPandas(
    listing,
    category_col="review_scores_rating",
    text_col="description",nlp=nlp).build().remove_terms(
        ENGLISH_STOP_WORDS,
    ignore_absences=True)
# html=st.produce_sc

