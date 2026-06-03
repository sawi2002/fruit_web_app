import streamlit as st

st.title("🍎 Fruit Web App")

fruit = st.selectbox(
    "Select a Fruit",
    ["Apple", "Banana", "Mango", "Orange"]
)

st.write("You selected:", fruit)
