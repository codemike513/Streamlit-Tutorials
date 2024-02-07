import folium
import streamlit as st
from streamlit_folium import folium_static

st.title('Mapping Your Location')

col1, col2 = st.columns(2)
latitude, longitude  = col1.number_input('Enter Latitude'), col2.number_input('Enter Longitude')
loc = (latitude, longitude)

map = folium.Map(location=loc, zoom_start=9)
folium.Marker(loc).add_to(map)
folium_static(map)
