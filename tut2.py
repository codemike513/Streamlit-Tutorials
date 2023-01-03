import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-2 Learning Display Elements")
st.markdown('''
There are a few ways to display data (tables, arrays, data frames) in Streamlit apps, which can be used to write anything from text to tables.
- Write -> Display tables, dataframes, plots
- Dataframe ->  To display data in Dataframe formats (allows to sort values)
- Table ->  To display data in Table formats
- Metric -> To displayt metrics of different values
''')
st.markdown('---')

st.write("## Hello! This is Markdown Script using write function")

st.write("Dataframe")
df = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5], "Column 2": [6, 7, 8, 9, 10]})
st.dataframe(df)

st.write('Table')
tab = pd.DataFrame({"Fruits": ['Apple', 'Banana', 'Mango', 'Orange'], "Veggies": [
                   'Potato', 'Lady Finger', 'Cabbage', 'Bottle Gourd']})
st.table(tab)

st.markdown('---')
st.write("Numpy and Highlighting")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.markdown('---')
st.write('## Metrics')
st.metric(label="Wind Speed", value="120 ms⁻¹", delta="1.4ms⁻¹")
st.metric(label="Temperature", value="40⁰ C", delta="-3.1⁰ C")
