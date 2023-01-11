import streamlit as st
import time as ts
from datetime import time

st.set_page_config(layout='wide')

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-7 Streamlit Layout")
st.markdown('''
- Set Page Config -> Changes the layout of App to wide/narrow etc.
- Columns -> Place Widgets Side by Side
- Expander -> Conserve Space by hiding away large content
- Container -> Use Layout features as form of Container
''')
st.markdown('---')


st.title('A Registration Form Layout')

first, last = st.columns(2)

first.text_input('First Name')
last.text_input('Last Name')

email, mob = st.columns([3, 1])
email.text_input('E-mail ID')
mob.text_input('Mobile Number')

user, pw, pw2 = st.columns(3)
user.text_input('Username')
pw.text_input('Password', type='password')
pw2.text_input('Retype your Password', type='password')

st.markdown('')

ch, bl, sub = st.columns(3)
ch.checkbox('I Agree')
sub.button('Submit')

st.markdown('---')
st.title('Expander')

with st.expander('Expand This Menu'):
    st.write('This is an Expander')
    if st.button('Hurray'):
        st.balloons()

st.markdown('---')

st.title('Container Example')


def my_widget(key):
    st.subheader('Hello There!')
    return st.button('Click Me ' + key)


clicked = my_widget('First')

my_expander = st.expander('Expand', expanded=True)
with my_expander:
    clicked = my_widget('Second')

with st.sidebar:
    clicked == my_widget('Third')
