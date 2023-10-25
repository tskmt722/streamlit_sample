import streamlit as st

st.set_page_config(
    layout = 'wide'
)

st.header('How to layout your streamlit app')

# サイドバー
st.sidebar.header('Input')
q1_name = st.sidebar.text_input('What is your name?')
q2_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊'])
q3_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# エキスパンダー
with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png')

# 出力
st.subheader('Output')

col1, col2, col3 = st.columns(3)

with col1:
    if q1_name != '':
        st.write(f':wave: Hello {q1_name}!')
    else:
        st.write(':point_left: Please enter you **name**!')

with col2:
    if q2_emoji != '':
        st.write(f'{q2_emoji} is your favorite **emoji**!')
    else:
        st.write(':point_left: Please choose an **emoji**!')

with col3:
    if q3_food != '':
        st.write(f':fork_and_knife: **{q3_food}** is your favorite **food**!')
    else:
        st.write(':point_left: Please choose your favorite **food**!')
