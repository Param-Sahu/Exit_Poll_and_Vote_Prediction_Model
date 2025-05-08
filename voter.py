import streamlit as st
import pickle
import numpy as np

# Load the trained AdaBoost model
with open('voter_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Voter Prediction App")
st.write("Enter voter information below to predict their vote (Labour or Conservative).")

# Input form using number_input and selectbox
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ("male", "female"))
economic_condition_national = st.number_input("Economic Condition (National)", min_value=1, max_value=5, value=3)
economic_condition_household = st.number_input("Economic Condition (Household)", min_value=1, max_value=5, value=3)
blair_rating = st.number_input("Rating for Blair", min_value=1, max_value=5, value=2)
hague_rating = st.number_input("Rating for Hague", min_value=1, max_value=5, value=2)
europe_opinion = st.number_input("Europe Opinion", min_value=1, max_value=11, value=3)
political_knowledge = st.selectbox("Political Knowledge (0 = Low, 3 = High)", [0, 1, 2, 3])

# Convert categorical variables
gender_numeric = 1 if gender == "male" else 0

# Feature vector (ensure the order matches your model input)
features = np.array([[age,  economic_condition_national,
                      economic_condition_household,
                        blair_rating, hague_rating, europe_opinion, political_knowledge,gender_numeric]])

# Predict button
if st.button("Predict Vote"):
    prediction = model.predict(features)[0]
    result = "Labour" if prediction == 1 else "Conservative"
    st.success(f"The voter is predicted to vote for: **{result}**",icon="✅")
    st.balloons()
