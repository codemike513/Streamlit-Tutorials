import streamlit as st
import time as ts
from datetime import time

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-6 File Uploader and Normal Animations")
st.markdown('''
- File Uploader -> To upload various types of files
- Progress -> A Progress Bar to show progress of anything
- Balloons -> To show Balloon Animation
''')
st.markdown('---')

st.title('Uploading Files')

img = st.file_uploader('Please Upload an Image', type=[
                       'png', 'jpg', 'jpeg', 'webp'])
if img is not None:
    st.image(img)

st.markdown('---')

pdf = st.file_uploader('Please Upload a Pdf/Word file', type=['pdf', 'word'])
if pdf is not None:
    st.write(pdf)

st.markdown('---')

vid = st.file_uploader('Please Upload a Video', type='mp4')

if pdf is not None:
    st.video(vid)

st.markdown('---')

aud = st.file_uploader('Please Upload an Audio', type='mp3')

if pdf is not None:
    st.audio(aud)

st.markdown('---')

st.markdown('### Multiple Files')

images = st.file_uploader('Please Upload Multiple Images', type=[
                          'png', 'jpg'], accept_multiple_files=True)
if images is not None:
    for img in images:
        st.image(img)

st.markdown('---')

st.title('Progress Bar')
if st.button('Show Progress Bar'):
    bar = st.progress(0)
    for i in range(100):
        v = bar.progress((i+1))
        ts.sleep(0.1)

st.markdown('---')

st.title('Balloons')
if st.button('Show Balloons'):
    st.balloons()
