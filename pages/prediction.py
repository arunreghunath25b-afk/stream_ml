import streamlit as st
import pickle
import os

st.title("🌸 Iris Flower Prediction")

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
model_path = os.path.join(BASE_DIR, "iris_model.pkl")

# Load model
with open(model_path, "rb") as file:
    model = pickle.load(file)

st.success("Model loaded successfully!")

# Inputs
sepal_length = st.number_input("Sepal Length", value=5.1)
sepal_width = st.number_input("Sepal Width", value=3.5)
petal_length = st.number_input("Petal Length", value=1.4)
petal_width = st.number_input("Petal Width", value=0.2)

if st.button("Predict"):

    input_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(input_data)

    flower_names = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }

    st.success(f"Predicted Flower: {flower_names[prediction[0]]}")