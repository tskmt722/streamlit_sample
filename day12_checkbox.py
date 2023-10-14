import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

val1_ice_cream = st.checkbox('Ice cream')
val2_coffee = st.checkbox('Coffee')
val3_cola = st.checkbox('cola')

if val1_ice_cream:
    st.write("Great! Here's some more :icecream:")

if val2_coffee:
    st.write("Okay, here's some coffee :coffee:")

if val3_cola:
    st.write("Here you go :cup_with_straw:")