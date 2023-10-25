import streamlit as st


st.title('st.experimental_get_query_params')

with st.expander('About this app'):
    st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

st.header('1. Instructions')
st.write('''
In the above URL bar of your internet browser, append the following:\n
`?name=Jack&surname=Beanstalk`\n
after the base URL\n
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`\n
such that it becomes\n
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())

st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()['firstname'][0]
surname = st.experimental_get_query_params()['surname'][0]

st.write(f'Hello, **{firstname} {surname}**, how are you?')
