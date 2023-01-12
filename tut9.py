import streamlit as st

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-9 Remove Hamburger Menu and Footer")
st.markdown('---')

st.subheader('Hamburger Menu and Footer Removed')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
