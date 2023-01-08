import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Welcome to Streamlit Tutorials !")

data = {
    'num': [x for x in range(1, 11)],
    'square': [x**2 for x in range(1, 11)],
    'twice': [x*2 for x in range(1, 11)],
    'thrice': [x*3 for x in range(1, 11)]
}

df = pd.DataFrame(data=data)

rad = st.sidebar.radio('Navigation', ['Home', 'Status Messages', 'About'])

if rad == 'Home':
    st.header("Tut-5 Sidebar with Navigation and Status Messages")
    st.markdown('''
    - Sidebar -> A side menu to choose contents and navigate to pages
    Status Messages
    - Error -> To show error
    - Success -> To show success/output
    - Info -> To show an information
    - Warning -> To show a warning
    - Exception -> To show an exception
    ''')
    st.markdown('---')

    col = st.sidebar.multiselect('Select a Column', df.columns)

    plt.plot(df['num'], df[col])
    st.pyplot()

if rad == 'Status Messages':
    st.header("Status Messages")
    st.markdown('---')

    st.error('Error')
    st.success('Show Success')
    st.info('Information')
    st.warning('This is a warning')
    st.exception(RuntimeError('This is an error -> Exception msg'))


if rad == 'About':
    st.header('About Page')
    st.subheader('These are Streamlit Tutorials to learn.')
