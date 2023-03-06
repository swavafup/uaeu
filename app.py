
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
#from google.colab import drive
import os
import streamlit as st
import warnings
warnings.filterwarnings('ignore')


st.title("FAQ Bot for UAEU")

user_input = st.text_input("Enter your Question here")

if st.button("Submit"):
    st.write("Answer:")
    query = user_input
    input_index = 'index.json'
    index = GPTSimpleVectorIndex.load_from_disk(input_index)
    response = index.query(query, response_mode="compact")
    st.write(response)
