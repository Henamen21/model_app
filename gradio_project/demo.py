import gradio as gr
import pickle
import os
import sklearn
import pandas as pd
 
# Define the input components and their labels
inputs = [
    gr.inputs.Radio(["Month-to-month", "One year", "Two year"], label="Contract"),
    gr.inputs.Dropdown(["Yes", "No"], label="Dependents"),
    gr.inputs.Dropdown(["Male", "Female"], label="gender"),
    gr.inputs.Dropdown(["Yes", "No"], label="SeniorCitizen"),
    gr.inputs.Dropdown(["Yes", "No"], label="Partner"),
    gr.inputs.Dropdown(["No phone service", "Yes", "No"], label="MultipleLines"),
    gr.inputs.Dropdown(["Yes", "No"],label="PhoneService"),
    gr.inputs.Dropdown(["DSL", "Fiber optic", "No"], label="InternetService"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="OnlineSecurity"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="OnlineBackup"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="DeviceProtection"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="TechSupport"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="StreamingTV"),
    gr.inputs.Dropdown(["No internet service", "Yes", "No"], label="StreamingMovies"),
    gr.inputs.Radio(["Month-to-month", "One year", "Two year"], label="Contract"),
]
""" 
                                                   '',
                                                   '',
                                                   '',
                                                   '',
                                                   '', '',
                                                   '',
                                                   '',
                                                   'PaperlessBilling',
                                                   'PaymentMethod' """
                                                   
""" 
    
    
    
    gr.inputs.Dropdown(["Yes", "No"], label="Paperless Billing"),
    gr.inputs.Radio(["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], label="Payment Method") """


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
def convert_to_df(Contract, Dependents, Gender , SeniorCitizen , 
                  Partner, MultipleLines , PhoneService , InternetService , 
                  OnlineSecurity , OnlineBackup , DeviceProtection , TechSupport ,
                  StreamingTV , ):
    # Create a list of lists from the input arguments
    data = [[Contract, Dependents, Gender , SeniorCitizen , 
             Partner , MultipleLines , PhoneService , InternetService , 
             OnlineSecurity, OnlineBackup , DeviceProtection , TechSupport ,
             StreamingTV, ]]
    
    # Create a dataframe from the data
    df = pd.DataFrame(data, columns=["Contract", "Dependents", "Gender" , "SeniorCitizen" , 
                                     "Partner" , "MultipleLines" , "PhoneService" , "InternetService" ,
                                     "OnlineSecurity" , "OnlineBackup" , "DeviceProtection" , "TechSupport" , 
                                     "StreamingTV"])
    print(df)
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


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""  
    
def word_count(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

# Load ml components from file
cwd = os.getcwd()
relative_path = "gradio_project\\pipeline.pkl"

absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)

# Reading Machine learning component file
with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)

print(ml_components)

iface = gr.Interface(
    fn=word_count, # the function to use
    inputs=gr.inputs.Textbox(lines=2, placeholder="Type some text here..."), # the input component
    outputs=[gr.outputs.Label(type="int", label="Number of words"), # the output components
             gr.outputs.Label(type="int", label="Number of characters")],
    title="Word Count", # the title of the interface
    description="A simple app that counts the number of words and characters in a text." # the description of the interface
)

iface.launch(share = "True") """