import streamlit as st
import pickle

st.title("_Iris model_ :blue[prediction] :sunglasses:")

# Load the trained model
model = pickle.load(open("iris_model.pkl", "rb"))

st.write("Model loaded successfully!")


