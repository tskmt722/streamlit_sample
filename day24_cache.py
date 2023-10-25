import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

@st.cache_data
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

t0 = time()

# キャッシュ使用
st.header('Using st.cache')
st.write(load_data_a())

t1 = time()
st.write(t1 - t0)

# キャッシュ未使用
st.header('Using st.cache')
st.write(load_data_b())

t2 = time()
st.write(t2 - t1)

