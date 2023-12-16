"""
Streamlit web app for project team communication.

This module provides a web interface for users to send feedback, report issues,
and get contact information for the project team.
"""

from datetime import datetime
import streamlit as st

# Constants
GITHUB_REPO_URL = "https://github.com/JordieB/khml_central"

def display_header():
    """
    Displays the header and introduction for the feedback page.
    """
    st.markdown('# How to Reach the Project Team')
    st.markdown("""
    Please reach out via the form to:
    * Report issues/bugs with this web app
    * Request updates and/or new features in tools, content
    * Submit data to be reviewed and added to the database
    * Have general feedback and/or ideas for this web app

    If you're more familiar with GitHub and/or want to contribute to the
    codebase, see repo in the links section of this page.
    """)

def feedback_form():
    """
    Displays and handles the feedback submission form.
    """
    st.markdown('## Feedback Form')
    with st.form(key='feedback_form'):
        feedback_text = st.text_area("Your feedback (bugs, ideas, etc.):",
                                help="Enter your feedback here")
        email = st.text_input(
            "Your email (optional):",
            help="Leave your email if you'd like us to reach out to you."
        )
        submit_button = st.form_submit_button("Submit Feedback")

        if submit_button:
            save_feedback(email, feedback_text)

def save_feedback(email: str, feedback_text: str):
    """
    Saves the provided feedback along with a timestamp.

    Args:
        email (str): The email address of the feedback provider.
        feedback_text (str): The content of the feedback.

    Note: This function currently lacks implementation details for saving data.
    """
    feedback_data = {
        'timestamp': datetime.now(),
        'email': email,
        'feedback': feedback_text,
    }
    # Implement saving to database or file here
    # Example: save_to_database(feedback_data)
    st.success("Thank you for your feedback!")

def display_contact_links():
    """
    Displays contact links for the project.
    """
    st.markdown('## Contact Links')
    st.markdown(f"* **App Repo:** [GitHub]({GITHUB_REPO_URL})")

def main():
    """
    Main function to display the Streamlit app.
    """
    display_header()
    feedback_form()
    display_contact_links()

if __name__ == '__main__':
    main()
