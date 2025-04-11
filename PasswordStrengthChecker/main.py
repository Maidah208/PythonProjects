import streamlit as st
import re

# Function to calculate password strength
def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        return "Very Strong 🔒"
    elif score == 4:
        return "Strong ✅"
    elif score == 3:
        return "Moderate ⚠️"
    elif score == 2:
        return "Weak ❗"
    else:
        return "Very Weak ❌"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        strength = check_password_strength(password)
        st.markdown(f"**Password Strength:** :{strength}")
        st.markdown("""
        **Tips for a strong password:**
        - Use at least 8 characters  
        - Combine uppercase and lowercase letters  
        - Include numbers  
        - Add special characters (!, @, #, etc.)
        """)
    else:
        st.warning("Please enter a password before checking.")
