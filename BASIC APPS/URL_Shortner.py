import streamlit as st
import pyshorteners
import pyperclip

shortener = pyshorteners.Shortener()


def copying():
    pyperclip.copy(shortened_url)


st.markdown("<h1 style='text-align: center;'>URL SHORTNER</h1>",
            unsafe_allow_html=True)

st.markdown('---')

form = st.form('name')
url = form.text_input('Enter URL Here')
s_btn = form.form_submit_button('SHORT')
if s_btn:
    shortened_url = shortener.tinyurl.short(url)
    st.markdown('<h3>Shorted URL</h3>', unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'>{shortened_url}</h6>",
                unsafe_allow_html=True)
    st.button('Copy URL', on_click=copying)
