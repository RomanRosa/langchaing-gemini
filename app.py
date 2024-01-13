import streamlit as st
from PyPDF2 import PdfFileReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai

from langchain.vectorstores import faiss
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))

def get_pdf_text(pdf_docs):
    text= ''
    for pdf in pdf_docs:
        pdf_reader= PdfFileReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks= text_splitter.split_text(text)
    return chunks