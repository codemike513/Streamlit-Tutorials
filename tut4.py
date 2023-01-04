import streamlit as st

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-4 Basic Interactive Widgets")
st.markdown('''
- Button -> A button with click functionality
- Text Input -> To take input of some text
- Text Area -> To take text input as paragraph
- Date Input -> To select a date
- Time Input -> To select time
- Checkbox -> To check a condition
- Radio -> Choose from different options
- Selectbox -> Choose from a dropdown list
- Multiselect -> Choose multiple values
- Slider -> Choose a value from sliding values
- Number Input -> Take numbers as input
''')
st.markdown('---')

st.button("Hello")
if st.button('Press Me'):
    st.write("Hello! How are You ?")

name = st.text_input('Enter your Name here:', max_chars=60)
st.write(f'Hello {name}')

address = st.text_area('Enter your Address here:', max_chars=200)
st.write(f'Your Address: {address}')

st.markdown('---')

st.date_input("Enter the date:")
st.time_input("Enter the time:")

if st.checkbox('You accept T&C', value=False, key='T&C'):
    st.write('Thank You')

st.markdown('---')

v1 = st.radio('Colors', ['Red', 'Green', 'Blue',
              'Yellow'], index=2, key='colors')

v2 = st.selectbox('Colors', ['Red', 'Green', 'Blue',
                             'Yellow'], index=0, key='Color')

st.write(v1, v2)


v3 = st.multiselect('Colors', ['Red', 'Green', 'Blue',
                               'Yellow'], key='colour')

st.write(v3)

st.markdown('---')

st.slider('Age', min_value=18, max_value=60, step=2, key='Age')

st.number_input('Numbers', min_value=10, max_value=80, step=2)

st.number_input('Float Numbers', min_value=30.60, max_value=120.30, step=0.7)
