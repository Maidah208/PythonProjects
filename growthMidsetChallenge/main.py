import streamlit as st # Library for building web apps
import pandas as pd # Library for data manipulation
import os # Library for interacting with the operating system
from io import BytesIO # 'BytesIO' is used to create an in-memory file 

# Set up the app configuration
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Easily convert files between CSV and Excel formats while applying data cleaning and basic visualizations.")

# File uploader for CSV and Excel files
uploaded_files = st.file_uploader(
    "Upload CSV or Excel files:", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the file based on its extension
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue

        # Display file details
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")
        st.write(f"**File Type:** {file.type}")

        # Show preview of the data
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # Data cleaning options
        st.subheader("Data Cleaning")
        if st.checkbox(f"Enable cleaning options for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed successfully.")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values filled with column mean.")

        # Column selection for conversion
        st.subheader("Column Selection")
        selected_columns = st.multiselect(f"Select columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Generate visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include=["number"]).iloc[:, :2])

        # File conversion options
        st.subheader("File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                new_file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False)
                new_file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            st.success("Processing complete.")
           
            buffer.seek(0)
                
            # Download button
            st.download_button(
                label=f"Download {new_file_name}",
                data=buffer,
                file_name=new_file_name,
                mime=mime_type)
            st.success("Thank you for using Data Sweeper!")
                

