import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# 例1
st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, ' years old.')

# 例2
st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
    0.00, 100.00, (25.00, 75.00)
)
st.write('Values: ', values)

# 例3
st.subheader('Range time slider')
appointment = st.slider(
    'Schedule your appointment: ',
    value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for: ", appointment)

# 例4
st.subheader('Datetime slider')
start_time = st.slider(
    'When do you start?',
    value=datetime(2023, 10, 13, 12, 30),
    format="MM/DD/YY - HH:MM"
)
st.write('Start time: ', start_time)