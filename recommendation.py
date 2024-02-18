import streamlit as st

def display():
    faculty = st.session_state['top_prof_indices']
    # Define the details for each faculty member in a list of dictionaries
    faculty_details = []
    for idx, f in faculty.iterrows():
        print(f)
        faculty_details.append(
            {
                "name": f["Faculty Name"],
                "email": f["Email Category"],
                "major": f["Department"],
                "publication": "Google Scholar",
                "url": f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C22&as_vis=1&q={f['Faculty Name']}&btnG="
                
            }
        )


    # Display three boxes with faculty details
    for faculty in faculty_details:
        with st.container():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                # Make the name a button for navigation
                if st.button(faculty["name"]):
                    st.session_state['current_page'] = "Prof Cluster"
                    st.session_state['selected_prof'] = faculty["name"]
            with col2:
                st.markdown("**Email:**")
                st.write(faculty["email"])
            with col3:
                st.markdown("**Major:**")
                st.write(faculty["major"])
            with col4:
                st.markdown("**Publications:**")
                st.write(faculty["publication"])
            st.markdown("---")  # Separator line



    # Logic for when the 'Explore More' button is pressed
    if st.button('Explore More'):
        # Perform action, e.g., navigate to another page
        # st.write("click explore more")
        st.session_state['current_page'] = "Directory"

