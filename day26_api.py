import streamlit as st
import requests

# sidebar
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox(
    'Select an activity type',
    ['education', 'recreational',
    'social', 'diy', 'charity',
    'cooking', 'relaxation',
    'music', 'busywork']
)

http://www.boredapi.com/api/activity?social

# APIのURLを生成
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'

# オブジェクトを取得し、jsonファイルを読み込む
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()


# main
st.title(':basketball: Bored API app')

col1, col2 = st.columns(2)

with col1:
    with st.expander('About this app'):
        st.write('Are you bored? **The Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')

with col2:
    with st.expander('JSON data'):
        st.write(suggested_activity)

st.header('Suggested activity')

st.info(suggested_activity['activity'])

col_x, col_y, col_z = st.columns(3)

with col_x:
    st.metric(label='Number of Participants', value=suggested_activity['participants'])

with col_y:
    st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize())

with col_z:
    st.metric(label='Price', value=suggested_activity['price'])
