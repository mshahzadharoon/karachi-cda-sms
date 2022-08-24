import streamlit as st
import pandas as pd
pd.options.mode.chained_assignment = None
from collections import Counter
import plotly.graph_objects as go


#data = pd.read_csv(path,encoding="ISO-8859-1")
data = pd.read_csv('SMS_data.csv',encoding="ISO-8859-1")

##***Message Count Received**##
msg_count = data.groupby('Date_Received')['Message_body'].count().sort_values(ascending=False)    

spam_data = data[data['Label'] == 'Spam']
no_spam_data = data[data['Label'] == 'Non-Spam']

##***SPAM**##
spam_cnt = Counter()
for text in data["Message_body"].values:
    for word in text.split():
        spam_cnt[word] += 1
spam_cnt.most_common(20)

common_word_spam = pd.DataFrame(spam_cnt.most_common(25), columns=['Common Words Spam', 'count'])


##***NON-SPAM**##
from collections import Counter
no_spam_cnt = Counter()
for text in no_spam_data["Message_body"].values:
    for word in text.split():
        no_spam_cnt[word] += 1
no_spam_cnt.most_common(25)

common_word_no_spam = pd.DataFrame(no_spam_cnt.most_common(25), columns=['Common Words Non-Spam', 'count'])

def main():
    st.title('SMS Chat Analysis')
    Filter   = st.selectbox('Search By',['No of Messages','Spam Data Check']) 
    
    if Filter == 'No of Messages':
        button  = st.button('Show Results')
        
        if button:
            st.subheader("Number of Messages Recieved over Dates")
            st.line_chart(msg_count)
    else:
        filterby = st.selectbox('Filter By',data.Label.unique()) 
        button  = st.button('Show Results')

        if button:

            if filterby == 'Spam':
                st.subheader("Most Common Words (SPAM) uses in SMS Data")

                fig = go.Figure()
                fig = fig.add_trace(go.Scatter(x=common_word_spam["count"], y=common_word_spam["Common Words Spam"]))
                st.plotly_chart(fig)
      
              
            elif filterby == 'Non-Spam':
                st.subheader("Most Common Words (NON-SPAM) uses in SMS Data")
                subset  =  common_word_no_spam['Common Words Non-Spam'] #common_word_no_spam
                st.bar_chart(subset)    

    
if __name__ == '__main__':
    main()
    
