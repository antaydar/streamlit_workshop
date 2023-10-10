import streamlit as st
import pandas as pd
import numpy as np


# First lines of code to test streamlit
st.write("Hellow World!")
st.write("Hello World again!")

# Setting sidebar equal to a variable "a" so that conditional statements can be used for selected value in sidebar
a = st.sidebar.radio("Select one:", [1, 2])
if a==1:
    st.video("https://www.youtube.com/watch?v=yIYKR4sgzI8&list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe")
else:
    st.write("and again!")

# Creating columns
col1, col2 = st.columns(2)
col1.write("This is col1")
col2.write("This is col2")

# Some more widgets
st.checkbox("I agree")
st.multiselect("Buy:", ["apple", "banana", "milk"])
st.slider("Pick a number:", 0, 100)
st.time_input("Meeting time:")

# An example data from Uber
DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')
nrows = 100 # Number of rows to display

# Caching data so that it is not loaded again and again
@st.cache_data

# Defining a function to load data
def load_data(DATA_URL_, nrows_):
    data = pd.read_csv(DATA_URL_, nrows=nrows_)
    data = data.rename(columns={"Lat": "LAT", "Lon": "LON"})
    return data

# Calling the function to display data on the map
data = load_data(DATA_URL, nrows)   
st.dataframe(data)
st.map(data.loc[:, ["LAT", "LON"]])  

# Deploying the app
# First you have to update the repo. Push the app to github


