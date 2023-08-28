import streamlit as st
import tempfile
from PyreSparser import ResumeParser
import pandas as pd
from Classify_Resume.my_transformer_function import MyTransformer,clean_it
import nltk
nltk.download('popular')
nltk.data.path.append('/path/to/nltk_data')


# from sklearn.base import BaseEstimator, TransformerMixin
# import re
# from nltk.corpus import stopwords   
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=True)


if uploaded_file is not None:
    
    new_df = pd.DataFrame(columns=['file_name',
                               'resume_type',
                               'name',
                               'email',
                               'mobile_number',
                               'skills',
                               'college_name',
                                'degree',
                                'designation',
                                'experience',
                                'company_names',
                                'no_of_pages',
                                'total_experience'])
    
    
    for file in uploaded_file:
        ext = file.name.split('.')[-1]
        
        if ext == 'doc':    # doc files are not allowed
            continue
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(file.read())
            x=ResumeParser(tmp_file.name,ext).get_extracted_data()
            new_df.loc[len(new_df),list(x.keys())] = list(x.values())
        
        new_df.loc[len(new_df)-1,'file_name'] = file.name
        
        
        

if len(uploaded_file) == 1:    
    if new_df.iloc[0,1] == 'Reactjs':
        st.image('./images/react.webp')
    elif new_df.iloc[0,1] == 'Peoplesoft':
        st.image('./images/Peoplesoft.png')
    elif new_df.iloc[0,1] == 'SQL':
        st.image('./images/sql.png')
    elif new_df.iloc[0,1] == 'workday':
        st.image('./images/Workday.png')

    st.write(x)


elif len(uploaded_file)> 1:    
    st.write(new_df.dropna(axis=1))
    


