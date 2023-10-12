'''
    ボタンクリックで表示テキストを変える練習
'''

import streamlit as st

st.title("title")
st.header("header")
st.subheader("subheader")
st.write("write")
st.caption("caption")

if st.button('Please click here!'):
    st.write('Thank you!')
else:
    st.write('')
