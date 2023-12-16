"""
Streamlit web app page for explaining the purpose and features of KHML Central.

This module provides a user-friendly interface to explain what KHML Central is,
what it does, and how users can contribute and engage with its content.
"""

import streamlit as st

def display_header():
    """
    Displays the main title of the About page.
    """
    st.markdown('# About KHML Central')

def mission_statement():
    """
    Displays the mission statement of KHML Central.
    """
    st.markdown("""
    ## What

    KHML Central seeks to provide Kingdom Hearts Missing-Link fans with the
    most comprehensive and user-friendly online resource. The goal is to
    enhance your interaction with the game by providing up-to-date news,
    in-depth strategies, and essential tools and data to support your journey
    through Kingdom Hearts Missing-Link.
    """)

def features_and_sections():
    """
    Displays the features and sections available on KHML Central.
    """
    st.markdown("""
    ## How

    - **Updates & Announcements**: Latest news about Kingdom Hearts
        Missing-Link.
    - **Strategy Guides**: Comprehensive guides for challenging game aspects.
    - **Interactive Tools**: Tools for tracking progress and planning quests.
    - **Community Content**: Engage with fan art and lore discussions.
    - **Expansive Database**: Access game mechanics, character profiles, and 
        more.
    """)

def community_and_contribution():
    """
    Encourages community engagement and contributions.
    """
    st.markdown("""
    ## Community & Contributions

    KHML Central seeks to become a community space for players to contribute 
    their insights, content, and ideas. Whether it's through submitting new 
    information for the database, providing feedback on tools, or 
    participating in community discussions, your input helps KHML Central grow 
    and improve.

    Visit the Contact tab to reach out with questions, feedback, suggestions,
    or new data. We'd love to hear from you!
    """)

def display_footer():
    """
    Displays the footer noting the independent nature of KHML Central.
    """
    st.markdown("---")
    st.markdown("""
    *KHML Central is an independent fan-made project and is not affiliated
    with the official Kingdom Hearts brand or its creators.*
    """)

def main():
    """
    Main function to display the Streamlit app's About page.
    """
    display_header()
    mission_statement()
    features_and_sections()
    community_and_contribution()
    display_footer()

if __name__ == '__main__':
    main()
