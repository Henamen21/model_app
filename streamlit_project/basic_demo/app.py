import streamlit as st
import pandas as pd
import os

st.write("""# This is header

This is my interface

""")


sepal_height = st.number_input("Enter " , key = "sw")
sepal_width  = st.number_input("Enter " , key = "sh")

petal_height = st.number_input("Enter " , key = "ph")
petal_width = st.number_input("Enter " , key = "pw")

if st.button("predict"):
    st.text("done!")

