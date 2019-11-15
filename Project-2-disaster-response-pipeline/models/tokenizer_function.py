import re
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class Tokenizer(BaseEstimator, TransformerMixin):
    """ Tokenize transformer to be used in the pipeline
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.Series(X).apply(tokenize).values


def tokenize(text):
    # Normalize Text
    text=re.sub(r"[^a-zA-Z0-9]",' ',text.lower())
    # Tokenize
    words=word_tokenize(text)
    # Remove Stopwords
    words=[w for w in words if w not in stopwords.words('english')]
    # Lemmatize
    lemmatizer=WordNetLemmatizer()
    lemmed=[lemmatizer.lemmatize( w, pos='n').strip() for w in words]
    lemmed=[lemmatizer.lemmatize( w, pos='v').strip() for w in lemmed]

    return lemmed



