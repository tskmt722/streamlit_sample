import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command')

prog_bar = st.progress(0)

for i in range(100):
    time.sleep(0.02)
    prog_bar.progress(i + 1)

time.sleep(0.3)
st.balloons()

time.sleep(2)
prog_bar.empty()
st.button('Rerun')