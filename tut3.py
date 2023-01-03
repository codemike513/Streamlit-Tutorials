import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-3 Adding Plots and Media Widgets")
st.markdown('''
Plots and Maps
- Line Chart -> Make a Line Chart to compare dataset
- Area Chart -> Make an Area Chart to compare dataset
- Bar Chart -> Make a Bar Chart to compare dataset
- Scatter Plot -> Scatter values to visualize dataset
- Altair Chart -> Used to visualize dataset
- Graphviz Chart -> Use to make Flowcharts
- Map -> Show Maps using Latitude and Longitude values
Media Widgets
- Image -> Display an Image
- Audio -> Add audio files and play them
- Video -> Play Video files
''')
st.markdown('---')
st.markdown('## Data')
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

st.dataframe(data)
st.markdown('# Charts & Plots')
st.markdown('## Line Chart')
st.line_chart(data)

st.markdown('---')
st.markdown('## Area Chart')
st.area_chart(data)

st.markdown('---')
st.markdown('## Bar Chart')
st.bar_chart(data)

st.markdown('---')
st.markdown('## Scatter Plot')

plt.scatter(data['a'], data['b'])
plt.title('Scatter Plot')
st.pyplot()

st.markdown('---')
st.markdown('## Altair Chart')
alt_chart = alt.Chart(data).mark_circle().encode(
    x='a', y='b', tooltip=['a', 'b']
)
st.altair_chart(alt_chart, use_container_width=True)

st.markdown('---')
st.text("Flowcharts")
st.markdown('## Graphviz Chart')
st.graphviz_chart('''
digraph{
    Python -> ML
    ML -> DataScience
    ML -> AI
    DataScience -> Job
    AI -> Job
}
''')

st.markdown('---')

st.markdown('# Maps')
st.markdown('### Blank Map')
st.map()

st.markdown('---')
st.markdown('### Map with Latitude and Longitude Values')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.markdown('---')
st.markdown('### India Map with Latitude and Longitude Values')
map_data = pd.DataFrame(
    np.random.randn(500, 2) + [20.59, 78.96],
    columns=['lat', 'lon'])

st.map(map_data)

st.markdown('---')
st.markdown('### India Map with Latitude and Longitude Values')
map_data = pd.DataFrame({
    'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat': [41.868171, 44.979840, 38.357972, 39.030575],
    'lon': [-87.667458, -93.272474, -85.765187, -95.702548]})
st.map(map_data)


st.markdown('---')
st.markdown('# Media Widgets')
st.markdown('## Image')
st.image('data/image.jpg')
st.markdown('### Image with Caption')
st.image('data/image2.jpg', caption='This is my cat', width=400)

st.markdown('---')
st.markdown('## Audio')
st.audio('data/audio.mpeg')

st.markdown('---')
st.markdown('## Video')
st.video('data/video.mp4')