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

with st.form("Form 1", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    st.text_input('E-mail Address')
    st.text_input('Password', type='password')
    st.text_input('Confirm Password', type='password')
    day, month, year = st.columns(3)
    day.text_input('Day')
    month.text_input('Month')
    year.text_input('Year')
    s_btn = st.form_submit_button('Submit')
    if s_btn:
        if f_name == "" and l_name == "":
            st.warning('Please Fill Above Fields')
        else:
            st.success('Registration Successful')

st.markdown('---')
st.title('User Login')


form1 = st.form("Form 2", clear_on_submit=True)
email = form1.text_input('E-mail Address')
pw = form1.text_input('Password', type='password')
sb_btn = form1.form_submit_button('Submit')
if sb_btn:
    if email == "" and pw == "":
        form1.warning('Please Fill Above Fields')
    else:
        form1.success('Login Successful')
