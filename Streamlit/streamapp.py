import streamlit as st
st.title("Finley Forged's First Streamlit App")
name = st.text_input("Enter name")
if name : st.write(f"Hello , {name}!")
num = st.slider("Pick number" ,0 ,100)