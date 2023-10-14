import streamlit as st

st.header('st.multiselect')

favorite_colors = st.multiselect(
    'What are your favorite colors',
    ['Yellow', 'Red', 'Green', 'Blue'],
    default = ['Yellow', 'Red']
)

st.write('You selected:', favorite_colors)