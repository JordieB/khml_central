"""
Landing page
"""

import streamlit as st

st.markdown('# KHML Central')

# Intro blurb
container = st.container(border=True)
container.write(("***News, Strategies, Tools, Data***\n\n"
                 "KHML Central brings you the latest updates, in-depth "
                 "strategies, comprehensive guides, and data/tools for "
                 "Kingdom Hearts Missing-Link."))

# App feature showcase
st.markdown(("""
## Feature Showcase
* **Content Aggregation & Reviews**: Discover the latest on Kingdom Hearts,
    from official news to fan-contributed content, with insightful reviews.
* **Player Tools**: Access handy tools designed to enhance your gameplay
    experience.
* **Searchable Database**: Explore a rich database of game information, easily
    searchable for quick reference.
"""))

# CTA
st.success(("Don't let your light go out! Explore KHML Central now and join "
           "the community to help improve it using the Contact page!"))
