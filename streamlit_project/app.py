import streamlit as st
import pandas as pd
import os
import pickle 
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler 


st.write("""# Corporation Favorita Grocery

Please enter your records

""")

# Load ml components from file
cwd = os.getcwd()
relative_path = "streamlit_project\\ml.pkl"
absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)

with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)

pip = ml_components["pipline"]
print(ml_components["pipline"])
      
family_choose = ["AUTOMOTIVE", "BABY CARE" , "BEAUTY" , "BEVERAGES" , "BOOKS" , "BREAD/BAKERY ", "CELEBRATION" , "CLEANING" , "DAIRY",
"DELI" , "EGGS" , "FROZEN FOODS" , "GROCERY I" , "GROCERY II" , "HARDWARE"  , "HOME AND KITCHEN I" , "HOME AND KITCHEN II ",
"HOME APPLIANCES" , "HOME CARE" , "LADIESWEAR" , "LAWN AND GARDEN" , "LINGERIE" , "LIQUOR-WINE-BEER" , "MAGAZINES" ,"MEATS" ,
"PERSONAL CARE" , "PET SUPPLIES" , "PLAYERS AND ELECTRONICS" , "POULTRY" , "PREPARED FOODS ", "PRODUCE" , "SCHOOL AND OFFICE SUPPLIES ",
"SEAFOOD" ]

# For accepting input

store_nbr = st.slider("Select an Store number", min_value=1, max_value=54, value=10, step=1)
family = st.selectbox("family", family_choose , key = "fam" )
onpromotion = st.number_input("onpromotion" , key = "pro" )
date = st.date_input("Select a start date", )

# For presenting output
if st.button("predict"):
    
    inputs = [
                ["store_nbr" , "family", "onpromotion", "date"], 
              
                 [ store_nbr , family, onpromotion, date ], 
                  
            ]
    
    df = pd.DataFrame(inputs[1:], columns=inputs[0])
    
    df = df.set_index("date")
    df = df[["store_nbr" , "onpromotion"]]
    print(df)
    
    a = pip.predict(df)
    df["sales"] = a

    print(df)
    
    st.write(a)
    st.write(df)
    