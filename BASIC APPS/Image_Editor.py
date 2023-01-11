import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>",
            unsafe_allow_html=True)

st.markdown('---')

image = st.file_uploader('Upload your Image', type=['jpg', 'png', 'jpeg'])

info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()

if image is not None:
    img = Image.open(image)
    st.image(img)

    info.markdown("<h1 style='text-align: center;'>Information</h1>",
                  unsafe_allow_html=True)
    size.markdown(f'<h6>Size: {img.size}</h6>', unsafe_allow_html=True)
    mode.markdown(f'<h6>Mode: {img.mode}</h6>', unsafe_allow_html=True)
    format_.markdown(f'<h6>Format: {img.format}</h6>', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>Resizing</h1>",
                unsafe_allow_html=True)
    width = st.number_input('Enter Width', value=img.width)
    height = st.number_input('Enter Height', value=img.height)

    st.markdown("<h1 style='text-align: center;'>Rotation</h1>",
                unsafe_allow_html=True)
    degree = st.number_input('Enter Degree')

    st.markdown("<h1 style='text-align: center;'>Filters</h1>",
                unsafe_allow_html=True)
    filters = st.selectbox(
        'Filters', ['None', 'Blur', 'Detail', 'Emboss', 'Sharpen', 'Smooth'])

    btn = st.button('Submit')
    if btn:
        edited = img.resize((width, height)).rotate(degree)
        filtered = edited
        if filters != "None":
            if filters == 'Blur':
                filtered = edited.filter(BLUR)
            elif filters == 'Detail':
                filtered = edited.filter(DETAIL)
            elif filters == 'Emboss':
                filtered = edited.filter(EMBOSS)
            elif filters == 'Sharpen':
                filtered = edited.filter(SHARPEN)
            else:
                filtered = edited.filter(SMOOTH)
        st.image(filtered)
