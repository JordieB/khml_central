"""
Module for displaying the landing page of KHML Central using Streamlit.

This module uses Streamlit to create a landing page for KHML Central, a
fan-made project for the Kingdom Hearts Missing-Link game. It includes news,
tools, and a searchable database.
"""

import streamlit as st


def display_intro():
    """Displays the introduction section."""
    intro_text = (
        "***News, Strategies, Tools, Data***\n\nKHML Central brings you the "
        "latest updates, in-depth strategies, comprehensive guides, and "
        "data/tools for Kingdom Hearts Missing-Link."
    )
    intro_container = st.container(border=True)
    intro_container.write(intro_text)


def display_features():
    """Displays the feature showcase section."""
    features_text = (
        "## Feature Showcase\n"
        "* **Content Aggregation & Reviews**: Discover the latest on Kingdom "
        "Hearts, from official news to fan-contributed content, with "
        "insightful reviews.\n"
        "* **Player Tools**: Access handy tools designed to enhance your "
        "gameplay experience.\n"
        "* **Searchable Database**: Explore a rich database of game "
        "information, easily searchable for quick reference."
    )
    st.markdown(features_text)


def display_cta():
    """Displays the call-to-action section."""
    cta_text = (
        "Don't let your light go out! Explore KHML Central now and join the "
        "community to help improve it using the Contact page!"
    )
    st.success(cta_text)


def display_footer():
    """Displays the footer section."""
    footer_text = (
        "---\n*KHML Central is an independent fan-made project and is not "
        "affiliated with the official Kingdom Hearts brand or its creators.*"
    )
    st.markdown(footer_text)


def main():
    """Main function to display the landing page."""
    st.markdown('# KHML Central')
    display_intro()
    display_features()
    display_cta()
    display_footer()


if __name__ == '__main__':
    main()
