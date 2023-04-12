import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin



def clean_it(txt):
    txt = txt.replace('\t',' ')
    txt = txt.replace('\n',' ')
    
    txt = re.sub(r'http\S+', '', (txt))                                                       # removing links
    txt = re.sub('[^a-z ]','', txt.lower())                                                 # only need alphabets also converting to lower case letters for convenience
    # txt = txt.split()                           
    txt = word_tokenize(txt)                                                                # tokenizing each words
    txt = [WordNetLemmatizer().lemmatize(x) for x in txt if x not in stopwords.words() ]    # removing stopwords and using lemmatization for root words
    txt = [x for x in txt if len(x.strip())>2]                                              # removing words containing less than 2 letters
    
    return " ".join(txt)



class MyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, func=clean_it):
        self.func = func

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.apply(self.func)
    
    
    
