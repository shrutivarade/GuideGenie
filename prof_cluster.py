
import streamlit as st

def display():
    # Get the selected professor's name from session state
    selected_prof = st.session_state.get('selected_prof', 'No professor selected')
    # st.write(f"You selected: {selected_prof}")

    # Center-align the subheader with markdown and HTML
    st.markdown(f"<h2 style='text-align: center;'>Students from the City of Boston under Professor {selected_prof}:</h2>", unsafe_allow_html=True)
    
    # Sample data - replace with actual student data
    students = [
        {'name': 'Alice Smith', 'email': 'alice.smith@example.com'},
        {'name': 'Bob Jones', 'email': 'bob.jones@example.com'},
        {'name': 'Carol Johnson', 'email': 'carol.johnson@example.com'},
        {'name': 'David Brown', 'email': 'david.brown@example.com'}
        # Add more student data as needed
    ]

    # Display student information in 4 columns
    for student in students:
        # Create four columns
        cols = st.columns(4)
        with cols[0]:
            st.write(student['name'])
        with cols[1]:
            st.write(student['email'])
        with cols[2]:
            st.write(student['name'])  # If you have more data, replace this accordingly
        with cols[3]:
            st.write(student['email'])  # If you have more data, replace this accordingly

    
