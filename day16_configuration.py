import streamlit as st
from PIL import Image

image = Image.open('img/watch.png')
st.set_page_config(
    page_title="IWC", 
    page_icon=image, 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # streamlit★
         streamlit勉強用★
         """
     })

st.header('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')
st.code('''
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
''')


st.header('Configuration： Theme')
st.checkbox(label='Check')
st.slider(label='Slider')
st.selectbox(label='Choose Your Favourite', options=['Snowpeak', 'Rakuten', 'Toyota Motors'])
