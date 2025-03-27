import streamlit as st
st.title("welcome to wscode tech")
st.header('python')
st.subheader("java")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
        print("Hello")
        """)

import pandas as pd
dataset = pd.read_csv("Products.csv")
st.dataframe(dataset)

name = st.text_input("Enter your name")
fname = st.text_input("Enter your Father Name: ")
adr = st.text_area("Enter your Text: ")
classdata = st.selectbox("Enter Your Class:",(1,2,3,4,5,6) )

button = st.button("Done")
if button:
    st.markdown(f"""
Name:{name}
Father Name: {fname}
address: {adr}
class: {classdata}""")