import pandas as pd
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from textblob import TextBlob

# Sidebar contents
with st.sidebar:
    st.title('Sentiment Analysis App')
    st.markdown('''
    ## About
    This app is an NLP-powered and built using:            
    - [Streamlit](https://streamlit.io/)
    - [TextBlob](https://textblob.readthedocs.io/en/dev/)            
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ in Streamlit')

st.header('Sentiment Analysis')
with st.container():

    def analyze(x):
        if x >= 0.5:
            st.toast('Its a Positive sentiment!', icon='😎')
            return 'Positive'
        elif x <= -0.5:
            st.toast('Its a Negative sentiment!', icon='😢')
            return 'Negative'
        else:
            st.toast('Its a Neutral sentiment!', icon='😐')
            return 'Neutral'

    def clear_text():
        st.session_state["text"] = ""    
    text = st.text_input('Please enter text here: ', key="text")

    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        result = round(blob.sentiment.polarity,2)
        st.write('Sentiment: ',analyze(result))
        st.button("Clear", on_click=clear_text)
    
    


