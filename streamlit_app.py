import streamlit as st
import requests

st.title("🧠Smart AI Nutrition Assistant")

# User Details
st.header("👤 Your Info")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)

# Text & Image Inputs
st.header("📝 Describe Your Food Goal or Preferences")
text = st.text_area("What do you want from your meal plan?")

image = st.file_uploader("📸 Optionally upload a food image", type=["jpg", "jpeg", "png"])

if st.button("🎯 Generate Personalized Meal Plan"):
    data = {
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "text": text
    }

    files = {"image": image} if image else None
    url = "http://localhost:8000/personalized-meal-plan"

    res = requests.post(url, data=data, files=files)
    result = res.json()
    
    st.subheader("🧠 Generated Plan")
    st.write(result.get("plan"))
    st.subheader("🔍 Prompt Sent to Gemini")
    st.code(result.get("prompt"))