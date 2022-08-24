import streamlit as st
import pandas as pd
#import numpy as np
#import re
#import nltk
#import spacy
import string
pd.options.mode.chained_assignment = None

#data = pd.read_csv('C:/Users/User/Desktop/SMS_data1.csv')
#path = 'C:/Users/User/Karachi ai/Class5/Assignment/SMS_data.csv'
#with open(path, encoding="utf8", errors='ignore') as data:
#data = pd.read_csv(path,encoding="ISO-8859-1")
data = pd.read_csv('SMS_data.csv',encoding="ISO-8859-1")

####*******####
data["text_lower"] = data["Message_body"].str.lower()
####*******####

data.drop(["text_lower"], axis=1, inplace=True)

PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    """custom function to remove the punctuation"""
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

data["text_wo_punct"] = data["Message_body"].apply(lambda text: remove_punctuation(text))
####*******####

from nltk.corpus import stopwords
", ".join(stopwords.words('english'))


####*******####
STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

data["text_wo_stop"] = data["text_wo_punct"].apply(lambda text: remove_stopwords(text))
####*******####

from collections import Counter
cnt = Counter()
for text in data["text_wo_stop"].values:
    for word in text.split():
        cnt[word] += 1
cnt.most_common(20)

def main():
    st.title('SMS Chat Analysis')
    filterby = st.selectbox('Filter By',data.Label.unique()) 
    button = st.button('Show Results')
    
    
    if button:
        subset = data[data['Label'] == filterby]
        st.table(subset)
        
#    if button:
        #subset1 = 

if __name__ == '__main__':
    main()
    
