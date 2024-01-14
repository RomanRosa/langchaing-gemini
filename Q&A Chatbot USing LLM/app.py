# Q&A ChatBot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() # Take Environment Variables

import streamlit as st
import os


## Function to load OpenAI Model and Get Responses

def get_openai_response(question):
    llm= OpenAI(openai_api_key= os.getenv('OPENAI_API_KEY'), temperature= 0.5)
    response= llm(question)
    return response


## Initialize Our Streamlit App

st.set_page_config(page_title= 'Q&A Demo')

st.header('LangChain Application')

input= st.text_input('Input: ', key= 'input')
response= get_openai_response(input)

submit= st.button('Ask The Question:')

## If Ask Button Is Clicked

if submit:
    st.subheader('The Response Is')
    st.write(response)
