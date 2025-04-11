import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Select at least one character type!"

    return ''.join(random.choice(characters) for _ in range(length))


# Streamlit UI
st.title("🔐 Password Generator")

length = st.slider("Select password length", min_value=4, max_value=32, value=12)
use_uppercase = st.checkbox("Include uppercase letters", value=True)
use_digits = st.checkbox("Include numbers", value=True)
use_special = st.checkbox("Include special characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_digits, use_special)
    st.text_input("Your Generated Password", value=password, type="default")
