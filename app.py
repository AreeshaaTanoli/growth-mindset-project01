# Imports (MUST BE AT THE TOP)
import streamlit as st

# Set up the app
st.set_page_config(page_title="FitLife Tracker", layout="wide")

# Other imports
import pandas as pd
import plotly.express as px
import random

# Custom CSS for responsiveness and styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        width: 100%;  /* Make buttons responsive */
    }
    .stHeader {
        color: #2c3e50;
    }
    @media (max-width: 600px) {
        /* Adjust font size for smaller screens */
        .stTitle {
            font-size: 24px !important;
        }
        .stHeader {
            font-size: 20px !important;
        }
        .stText {
            font-size: 16px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and description
st.title("🏋️‍♂️ FitLife Tracker")
st.write("Track your health and fitness goals with personalized plans and insights.")

# User Profile
with st.sidebar:
    st.header("👤 User Profile")
    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    weight = st.number_input("Weight (kg)", min_value=1, value=70)
    height = st.number_input("Height (cm)", min_value=1, value=170)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])

    # BMI Calculation
    bmi = weight / ((height / 100) ** 2)
    st.write(f"**BMI:** {bmi:.2f}")

# Workout Plans
st.header("💪 Workout Plans")
if goal == "Weight Loss":
    st.write("**Plan:** Cardio and strength training 4 times a week.")
elif goal == "Muscle Gain":
    st.write("**Plan:** Weightlifting and protein-rich diet.")
else:
    st.write("**Plan:** Maintain current routine with balanced workouts.")

# Diet Tracker
st.header("🍎 Diet Tracker")
meal = st.text_input("What did you eat today?")
if meal:
    st.write(f"**Meal:** {meal}")

# Water Intake Tracker
st.header("💧 Water Intake Tracker")
water_intake = st.slider("Glasses of water today", min_value=0, max_value=15, value=5)
st.write(f"**Water Intake:** {water_intake} glasses")

# Mental Health Tracker
st.header("🧠 Mental Health Tracker")
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Stressed", "Neutral"])
st.write(f"**Mood:** {mood}")

# Daily Tips and Motivational Quotes
st.header("💡 Daily Tips")
tips = [
    "Drink at least 8 glasses of water daily.",
    "Take a 10-minute walk after meals.",
    "Practice deep breathing to reduce stress.",
    "Get at least 7-8 hours of sleep every night.",
    "Include protein in every meal for muscle repair."
]
st.write(f"**Tip of the Day:** {random.choice(tips)}")

# Progress Visualization
st.header("📊 Progress Visualization")
progress_data = pd.DataFrame({
    "Week": [1, 2, 3, 4],
    "Weight": [70, 69, 68, 67]
})
fig = px.line(progress_data, x="Week", y="Weight", title="Weight Loss Progress")
st.plotly_chart(fig, use_container_width=True)  # Make chart responsive

# AI-Powered Suggestions
st.header("🤖 AI-Powered Suggestions")
if st.button("Get Suggestions"):
    if goal == "Weight Loss":
        st.write("**Suggestion:** Try adding 20 minutes of cardio to your routine.")
    elif goal == "Muscle Gain":
        st.write("**Suggestion:** Increase your protein intake and focus on compound lifts.")
    else:
        st.write("**Suggestion:** Maintain a balanced diet and regular exercise routine.")

# Footer
st.markdown("---")
st.write("Made with ❤️ by [Areesha Tanoli]")