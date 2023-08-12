import streamlit as st
import pandas as pd
import os
import pickle 
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler 

# Company image
st.image("https://upload.wikimedia.org/wikipedia/commons/0/0f/Corporaci%C3%B3n_Favorita_Logo.png?20161217003545")

st.write("""# Corporation Favorita Grocery """)

# Write a subheader
st.subheader("Enter your records")

# Load ml components from file
cwd = os.getcwd()
relative_path = "gradio_project\\pipeline.pkl"

absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)

# Reading Machine learning component file
with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)

pip = ml_components

print(pip)

inputs = [
    ["gender" , "SeniorCitizen", "Partner",
    'Dependents', 'PhoneService', 'MultipleLines',
    'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract',
    'PaperlessBilling', 'PaymentMethod',
    'tenure', 'MonthlyCharges', 'TotalCharges'
    ], 

    [ "Male" , "No", "No",
    "No" , "Yes", "No",
    "Fiber optic" , "No",
    "No" , "No",
    "No" , "No",
    "Yes" , "Month-to-month",
    "Yes", "Electronic check",
    12 , 23 ,32
    ], 

    ]

df = pd.DataFrame(inputs[1:], columns=inputs[0])
st.write(df)
pred = pip.predict(df)

print(pred)
