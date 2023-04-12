import pickle
from .my_transformer_function import MyTransformer,clean_it
import os


def classify_resume(text):
    
    module_dir = os.path.dirname(os.path.abspath(__file__))
    
    pickle_path = os.path.join(module_dir, 'pipeline.pkl')
    
    with open(pickle_path, 'rb') as f:
        pipeline = pickle.load(f)
    
    # pipeline = pickle.load(open('pipeline.pkl','rb'))
    
    return pipeline.predict(text)