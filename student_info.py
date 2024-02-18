import streamlit as st
from model import recommend_professors_gemini
import pandas as pd
import ast

def display():
    st.write('Welcome to the Student info Page!')

    # Inject custom CSS for styling
    st.markdown("""
    <style>
    /* Apply CSS to the main content area where the form is displayed */
    .stTextInput input {
        color: #C3EBEF;
        background-color: #003450;
        border-radius: 5px;
    }
    .stTextInput label {
        color: #C3EBEF;
    }
    .stTextArea textarea {
        color: #C3EBEF;
        background-color: #003450;
        border-radius: 5px;
    }
    .stTextArea label {
        color: #C3EBEF;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("student_info"):
        name = st.text_input("Name", placeholder="Name")
        email = st.text_input("Email", placeholder="john.doe@xyz.com")
        major = st.text_input("Major", placeholder="Major")
        aoi = st.text_input("Area of interest", placeholder="Area of interest")
        about_you = st.text_area("About you", placeholder="About you")
        submitted = st.form_submit_button("Submit")

        professors_data = pd.read_csv("data_with_embedding.csv")
        professors_data['Gemini_Embedding'] = professors_data['Gemini_Embedding'].apply(lambda x: [float(i) for i in ast.literal_eval(x)])

        if submitted:
            # st.session_state['student_name'] = name
            # st.session_state['student_name'] = aoi
            # st.session_state['student_name'] = about_you
            # st.session_state['student_name'] = major

            top_prof_indices = recommend_professors_gemini(professors_data, name, aoi, about_you, major)
            print(top_prof_indices)

            st.session_state['top_prof_indices'] = top_prof_indices
            print(f'Top Prof Indices: {st.session_state["top_prof_indices"]}')

            st.session_state['current_page'] = "Option"
            # Handle the form submission as needed

