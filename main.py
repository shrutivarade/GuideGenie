import streamlit as st
import home, student_info, option, error, recommendation, directory, prof_cluster

# Layout for navigation (horizontal sidebar buttons)
st.title("Guide Genie")

# A dictionary mapping page names to functions
PAGES = {
    "Home": home.display,
    "Student Info": student_info.display,
    "Option": option.display,
    "Error": error.display,
    "Recommendation": recommendation.display,
    "Directory": directory.display,
    "Prof Cluster": prof_cluster.display
}
# Initialize the current page to home if not previously set
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "Home"


# Your logic to display pages based on the current_page value
if st.session_state['current_page'] == "home":
    home.display()
elif st.session_state['current_page'] == "prof_cluster":
    prof_cluster.display()

# Define a function to navigate to a page
def navigate(page_name):
    st.session_state['current_page'] = page_name
# Accessing keys by index
page_name = list(PAGES.keys())
button_col1, button_col2 = st.columns(2)
for i in range (0,1):
    with locals()[f"button_col{i % 2 + 1}"]:
        if st.button(page_name[i]):
                navigate(page_name[i])

# Display the selected page
PAGES[st.session_state['current_page']]()



