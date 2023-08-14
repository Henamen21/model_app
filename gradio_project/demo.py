import gradio as gr
import pickle
import os
import sklearn
import pandas as pd
 
# Define the input components and their labels
inputs = [
    gr.inputs.Dropdown(["Male", "Female"], label="gender"),
    gr.inputs.Dropdown(["Yes", "No"], label="SeniorCitizen"),
    gr.inputs.Dropdown(["Yes", "No"], label="Partner"),
    gr.inputs.Dropdown(["Yes", "No"], label="Dependents"),
    gr.inputs.Dropdown(["Yes", "No"],label="PhoneService"),
    gr.inputs.Dropdown(["No phone service", "Yes", "No"], label="MultipleLines"),    
    gr.inputs.Dropdown(["DSL", "Fiber optic", "No"], label="InternetService"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="OnlineSecurity"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="OnlineBackup"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="DeviceProtection"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="TechSupport"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="StreamingTV"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="StreamingMovies"),
    gr.inputs.Radio(["Month-to-month", "One year", "Two year"], label="Contract"),
    gr.inputs.Dropdown(["Yes", "No"], label="PaperlessBilling"),
    gr.inputs.Radio(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], label="PaymentMethod"),
    gr.inputs.Number(default=0,  label="tenure"),
    gr.inputs.Number(default=0,  label="MonthlyCharges"),
    gr.inputs.Number(default=0,  label="TotalCharges")  
]                                                  

# Define the output component and its label
output = gr.outputs.Label(label="Churn Prediction") 

# Load ml components from file
cwd = os.getcwd()
relative_path = "gradio_project\\pipeline.pkl"

absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)
print(inputs)

# Reading Machine learning component file
with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)

print(ml_components)

# Define the conversion function
def convert_to_df(gender, SeniorCitizen, Partner , Dependents , 
                PhoneService , MultipleLines , InternetService , OnlineSecurity, 
                OnlineBackup , DeviceProtection , TechSupport ,
                StreamingTV , StreamingMovies , Contract , PaperlessBilling , PaymentMethod , 
                tenure , MonthlyCharges , TotalCharges):
    # Create a list of lists from the input arguments
    data = [[gender, SeniorCitizen, Partner , Dependents , 
            PhoneService , MultipleLines , InternetService , OnlineSecurity, 
            OnlineBackup , DeviceProtection , TechSupport ,
            StreamingTV , StreamingMovies , Contract, PaperlessBilling , PaymentMethod , 
            tenure , MonthlyCharges , TotalCharges]]
    
    # Create a dataframe from the data  
    df = pd.DataFrame(data, columns=["gender", "SeniorCitizen", "Partner" , "Dependents" , 
                "PhoneService" , "MultipleLines" , "InternetService" , "OnlineSecurity", 
                "OnlineBackup" , "DeviceProtection" , "TechSupport" ,
                "StreamingTV" , "StreamingMovies" , "Contract","PaperlessBilling" , "PaymentMethod" , 
                "tenure" , "MonthlyCharges" , "TotalCharges"])
    print("check")
    print(df)
    print(ml_components.predict(df))
    # Return the dataframe
    return df

""" # Define the prediction function   
def predict_churn(*args):
    # Convert the input arguments into a dataframe
    input_df = pd.DataFrame([args], columns=df.columns[:-1])
    
    # Make a prediction using the model 
    pred = ml_components.predict(input_df)[0]
    
    # Return the prediction as a string
    if pred == 0:
        return "No"
    else:
        return "Yes" """

# Create and launch the interface
iface = gr.Interface(fn=convert_to_df, inputs=inputs, outputs=output)
iface.launch(share = "True")
