import streamlit as st
from PyPDF2 import PdfReader, PdfWriter 

st.title("Merge Two PDF's")

first = st.file_uploader('Enter First File', ['pdf'], key='first')
second = st.file_uploader('Enter Second File', ['pdf'], key='second')

file_name = st.text_input('Enter Final File Name')

docs = [first, second]
merger = PdfWriter()

if st.button("MERGE"):
    for doc in docs:
        merger.append(doc)

s = merger.write(file_name)
merger.close()
