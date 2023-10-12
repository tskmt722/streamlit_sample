import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("st.write")

# 例1
st.subheader("Display text")
st.write("Hello, *World!* :sunglasses:")

# 例2
st.subheader("Display numbers")
st.write(1234)

# 例3
# DataFrameの準備
arr = np.array([[1,10], [2,20], [3,30], [4,40]])
columns = ["first column", "second column"]
df = pd.DataFrame(data=arr, columns=columns)

st.subheader("Display DataFrame")
st.write(df)

# 例4
st.subheader("Accept multiple arguments")
st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# 例5
df2 = pd.DataFrame (
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.subheader("Display charts")
st.write(c)

