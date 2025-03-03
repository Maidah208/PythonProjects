import streamlit as st

st.title("Unit Converter")  
st.markdown("### This app converts various units")  
st.write("Please select the type of conversion you would like to make from the dropdown menu below:")

category = st.selectbox("Select conversion type", ["Temperature", "Length", "Weight"])

def uniConverter(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return f"{value * 0.621371:.2f} miles"
        elif unit == "Miles to kilometers":
            return f"{value / 0.621371:.2f} kilometers"
        elif unit == "Centimeters to inches":
            return f"{value / 2.54:.2f} inches"
        elif unit == "Inches to centimeters":
            return f"{value * 2.54:.2f} cm"
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return f"{value * 2.20462:.2f} pounds"
        elif unit == "Pounds to kilograms":
            return f"{value / 2.20462:.2f} kg"
        elif unit == "Grams to ounces":
            return f"{value / 28.3495:.2f} ounces"
        elif unit == "Ounces to grams":
            return f"{value * 28.3495:.2f} grams"
        
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return f"{(value * 9/5) + 32:.2f} °F"
        elif unit == "Fahrenheit to Celsius":
            return f"{(value - 32) * 5/9:.2f} °C"
        elif unit == "Celsius to Kelvin":
            return f"{value + 273.15:.2f} K"
        elif unit == "Kelvin to Celsius":
            return f"{value - 273.15:.2f} °C"

if category == "Length":
    unit = st.selectbox("Select unit", ["Kilometers to miles", "Miles to kilometers", "Centimeters to inches", "Inches to centimeters"])
elif category == "Weight":
    unit = st.selectbox("Select unit", ["Kilograms to pounds", "Pounds to kilograms", "Grams to ounces", "Ounces to grams"])  
elif category == "Temperature":
    unit = st.selectbox("Select unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])

value = st.number_input("Enter value to convert")

if st.button("Convert"):
    result = uniConverter(category, value, unit)
    st.write(f"**The result is:** {result}")  
