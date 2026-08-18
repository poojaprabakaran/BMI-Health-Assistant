import streamlit as st
import google.generativeai as genai
import pandas as pd 
import os
from dotenv import load_dotenv
load_dotenv()

key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=key)

st.title("Health Assistant For Fitness 🤖")
st.subheader("Welcome to health assistance! Place to get information on fitness using BMI value📋")

st.sidebar.subheader("Height")
height = st.sidebar.number_input('Enter the height in meters:', min_value=0.0, format="%.2f")

st.sidebar.subheader("Weight")
weight = st.sidebar.number_input('Enter the weight in kg:', min_value=0.0, format="%.2f")

# BMI calculation
if height > 0 and weight > 0:
   bmi = weight/(height**2)
   st.sidebar.success(f"BMI value is {round(bmi,2)}")
else:
    st.sidebar.warning('Please enter positive values.')

# Generate result

input= st.text_input('Ask your question here🔍')

model = genai.GenerativeModel('gemini-3.6-flash')

def get_response(input,bmi):
    if input:
        prompt = f"""You are a health and fitness assistant.
        The user's BMI is {bmi:.2f}.
        User's question: {input}.
        Answer the user's question based on their BMI where relevant.
        You can provide general fitness, diet, and health lifestyle suggestions.
        If medications related questions are asked always give a disclaimer to consult with thier physician.
        Do not diagnose medical conditions.
        """
        response = model.generate_content(prompt)
        return response.text
    
if st.button("Click here🎯"):
        if input:
          with st.spinner('It is loading..'):
            result = get_response(input,bmi)
            st.write(result)
        else:
            st.warning('Please enter a question')