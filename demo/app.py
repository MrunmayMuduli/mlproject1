import streamlit as st
from helper import add_numbers, subtract_numbers

st.title("🚀 Streamlit Debug Demo")
st.write("This is a sample Streamlit app you can debug in VS Code.")

x = st.number_input("Enter first number", value=10)
y = st.number_input("Enter second number", value=20)

if st.button("Add"):
    result = add_numbers(x, y)
    st.success(f"Result = {result}")

if st.button("Subtract"):
    result = subtract_numbers(x, y)
    st.success(f"Result = {result}")
