import streamlit as st #type: ignore
from transformers import pipeline

pipe = pipeline('sentiment-analysis')

st.title("Sentiment-Analyzer")
user_input = st.text_input("Enter your text")

if st.button('Get Sentiment'):
    if user_input:
        result = pipe(user_input)

        st.write(result[0]['label'])

