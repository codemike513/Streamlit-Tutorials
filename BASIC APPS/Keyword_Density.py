import streamlit as st
import re

st.markdown("<h1 style='text-align: center;'>Keyword Density Checker</h1>",
            unsafe_allow_html=True)

st.markdown('---')

text = st.text_area('Paragraph')

words_dict = dict()

if st.button('Check Density'):
    col1, col2, col3 = st.columns(3)
    if text:
        col1.markdown(
            "<h3 style='text-align: center;'>Keywords</h3>", unsafe_allow_html=True)
        col1.markdown('---')
        col2.markdown(
            "<h3 style='text-align: center;'>Occurances</h3>", unsafe_allow_html=True)
        col2.markdown('---')
        col3.markdown(
            "<h3 style='text-align: center;'>Percentages</h3>", unsafe_allow_html=True)
        col3.markdown('---')

        sim_text = re.sub("[,.?!&*;:]", "", text)
        words = sim_text.lower().split()
        t_len = len(words)
        for word in words:
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
        keys = list(words_dict.keys())
        values = list(words_dict.values())
        for i in range(len(keys)):
            col1.markdown(
                f"<h5 style='text-align: center;'>{keys[i]}</h5>", unsafe_allow_html=True)
            col2.markdown(
                f"<h5 style='text-align: center;'>{values[i]}</h5>", unsafe_allow_html=True)
            col3.markdown(
                f"<h5 style= 'text-align: center;'>{round((values[i]/t_len*100))}%</h5>", unsafe_allow_html=True)
