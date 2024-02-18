# home.py in pages/primary directory
import streamlit as st
import pandas as pd

import numpy as np


def display():
    # Load the CSV data
    try:
        df = pd.read_csv("data_with_embedding.csv")  # Replace "faculty.csv" with your actual filename
    except FileNotFoundError:
        st.error("Error: The specified CSV file was not found. Please ensure it exists and is accessible.")
        exit()

    # Check for required columns
    required_columns = ["Faculty Name", "Title", "Department", "Email Category"]
    if not all(col in df.columns for col in required_columns):
        st.error("Error: The CSV file must contain the following columns: ", ", ".join(required_columns))
        exit()

    st.sidebar.header("Filters")

    departments = df["Department"].unique()

    titles = df["Title"].unique()

    departments = np.insert(departments, 0, "All", axis=0)
    titles = np.insert(titles, 0, "All", axis=0)


    department_filter = st.sidebar.selectbox("Filter by Department", departments)
    
    title_filter = st.sidebar.selectbox("Filter by Title", titles)

    # Apply filters to the data
    filtered_df = df.copy()
    if department_filter != "All":
        filtered_df = filtered_df[filtered_df["Department"] == department_filter]
    if title_filter != "All":
        filtered_df = filtered_df[filtered_df["Title"] == title_filter]

    # Display individual faculty information
    st.header("Faculty Information")

    for index, row in filtered_df.iterrows():
        st.write("Faculty Name:", row["Faculty Name"])
        st.write("Title:", row["Title"])
        st.write("Department:", row["Department"])
        st.write("Email:", row["Email Category"])
        st.write("url:", f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C22&as_vis=1&q={row['Faculty Name']}&btnG=")
        st.markdown("---")  # Add a separator between faculty entries

    # Optional enhancements:
    # - Add a search bar to filter faculty by name
    # - Enable sorting by different columns
    # - Implement visual formatting for better readability
    