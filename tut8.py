import streamlit as st
import time as ts
from datetime import time

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-8 Streamlit Forms")
st.markdown('''
- Form -> Creates a Form 
''')
st.markdown('---')

st.title('User Registration')

with st.form("Form 1"):
    col1, col2 = st.columns(2)
    col1.text_input('First Name')
    col2.text_input('Last Name')
    st.text_input('E-mail Address')
    st.text_input('Password', type='password')
    st.text_input('Confirm Password', type='password')
    day, month, year = st.columns(3)
    day.text_input('Day')
    month.text_input('Month')
    year.text_input('Year')
    st.form_submit_button('Submit')


st.markdown('---')
st.title('User Login')


form1 = st.form("Form 2")
form1.text_input('E-mail Address')
form1.text_input('Password', type='password')
form1.form_submit_button('Submit')
