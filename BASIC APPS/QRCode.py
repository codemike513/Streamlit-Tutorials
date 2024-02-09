import streamlit as st
import io
import pyqrcode
import png
from base64 import b64encode

def GenerateQR(string):
    img = pyqrcode.create(string)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode('ascii')
    print('QR Code Generation Successful')
    qr = 'data:image/png;base64, ' + encoded
    return qr

st.title('QR Code Generator')

text = st.text_input('Enter the Text:')
if text:
    st.image(GenerateQR(text))
