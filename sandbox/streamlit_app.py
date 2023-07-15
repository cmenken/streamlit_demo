import streamlit as st
st.title('My first app')

name = st.sidebar.text_input('Enter your name','')

# st.write(f'Hello {name}!')
st.write('Hello',name,'!')

