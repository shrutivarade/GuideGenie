import streamlit as st

def display():
    # st.title('Option Page')

    # Custom CSS to center text using Markdown
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    <p class="centered-text">Select the type of mentor you would like to have!</p>
    """, unsafe_allow_html=True)

    # st.write('Select the type of mentor you would like to have!')

    # Create two columns
    col1, col2, col3, col4 = st.columns([2,1,1,2])

    # Button 1: Faculty
    with col2:
        faculty = st.button("Academic Faculty", key="faculty_button")
        if faculty:
            # st.write("Navigating to the next page...")
            st.session_state['current_page'] = "Recommendation"

    # Button 2: Professional (Disabled)
    with col3:
        professional = st.button("Working Professional", disabled=True)
