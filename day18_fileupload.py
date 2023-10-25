import streamlit as st
import numpy as np
from PIL import Image

st.header('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:

    # 画像を開く
    image = Image.open(uploaded_file)

    # 三次元配列データとして渡す
    img_array = np.array(image)

    # 画像を埋め込む
    st.image(img_array, width=200)

else:
    st.info('☝️ Upload a Img file')