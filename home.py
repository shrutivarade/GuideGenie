import streamlit as st
import student_info

# Set the page to wide mode
st.set_page_config(layout="wide")

def display():
    # Custom CSS to simulate a navbar and position elements
    st.markdown("""
    <style>
    .logo {
        float: left;
        position: relative;
        padding: 15px 15px 15px 5px;
    }
    .nav {
        float: right;
        position: relative;
        padding: 10px 10px 10px 10px;
    }
    .centered {
        text-align: center;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 class="centered">Are you looking for a mentor?</h1>', unsafe_allow_html=True)

    # Create a header with 2 columns
    b_col1, b_col2, b_col3 = st.columns([1.5, 1, 1.5])
    with b_col2:
        # Displaying an image at the center
        st.image("gfx/genie_circle.png", use_column_width=True)

    # Next button or arrow
    if st.button('Next ➡'):
        # st.session_state['current_page'] = "About Us"
        st.session_state['current_page'] = "Student Info"
        # student_info.display()
    
if __name__ == "__main__":
    # Hide Streamlit watermark
    st.set_config(hide_streamlit_style=True)
    display()
