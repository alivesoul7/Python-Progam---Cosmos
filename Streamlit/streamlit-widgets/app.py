import streamlit as st

clicked = st.button("Calculator")
agree = st.checkbox("I agree to the terms")
fruit = st.selectbox("Favorite fruit", ["Apple" , "Banana","Mango"])
col1 , col2 = st.coloumns(2)
with col1: st.write("Left side")

col1,col2 = st.coloumns(2)
with col1:
    st.value("Left side")
with col2:
    st.value("Right side")