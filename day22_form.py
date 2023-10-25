import streamlit as st

st.title('st.form')

st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('Order your coffee'):

    q1_been = st.selectbox(
        'Coffee bean',
        ['Arabica', 'Robusta']
    )

    q2_roast = st.selectbox(
        'Coffee roast',
        ['Light', 'Medium', 'Dark']
    )

    q3_brewing = st.selectbox(
        'Brewing method',
        ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon']
    )

    q4_serve = st.selectbox(
        'Serving format',
        ['Hot', 'Iced', 'Frappe']
    )

    q5_milk = st.select_slider(
        'Mild intensity',
        ['None', 'Low', 'Medium', 'High']
    )

    q6_cup = st.checkbox('Bring own cup')

    submitted = st.form_submit_button()

if submitted:

    ans = f'''
    :coffee: You have ordered:
    - Coffee bean: `{q1_been}`
    - Coffee roast: `{q2_roast}`
    - Brewing: `{q3_brewing}`
    - Serving type: `{q4_serve}`
    - Milk: `{q5_milk}`
    - Bring own cup: `{q6_cup}`
    '''
    st.write(ans)
else:
    st.write('☝ Place your order!')

# form2

st.header('2. Example of object notation')
with st.form('Select a value'):
    
    value = st.slider(
        'Select a value',
        0, 100, step=5
    )
    submitted2 = st.form_submit_button()

if submitted2:
    st.write('Selected value: ', value)
else:
    st.write('Selected value: ', 0)