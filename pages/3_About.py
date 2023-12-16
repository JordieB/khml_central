"""
Explain to new users what app is for, does, etc.
"""

import streamlit as st

# About Page Title
st.markdown('# About KHML Central')

# Mission Statement
st.markdown("""
## What

KHML Central seeks to provide Kingdom Hearts Missing-Link fans with the most 
comprehensive and user-friendly online resource. The goal is to enhance your 
interaction with the game by providing up-to-date news, in-depth strategies, 
and essential tools and data to support your journey through Kingdom Hearts 
Missing-Link.
""")

# Features and Sections
st.markdown("""
## How

- **Updates & Announcements**: Get the latest news and announcements about
    Kingdom Hearts Missing-Link as soon as they're released.
- **Strategy Guides**: Benefit from comprehensive strategy guides that help 
    you overcome the most challenging aspects of the game.
- **Interactive Tools**: Utilize our interactive tools to track your progress, 
    plan your quests, and manage your in-game resources.
- **Community Content**: Engage with content created by the community, from 
    fan art to deep-dive lore discussions.
- **Expansive Database**: Access an extensive database filled with game 
    mechanics, character profiles, item details, and more.
""")

# Community and Contribution >> CTA - Contact page
st.markdown("""
## Community & Contributions

KHML Central seeks to become a community space for players to contribute their 
insights, content, and ideas. Whether it's through submitting new information 
for the database, providing feedback on tools, or participating in community 
discussions, your input helps KHML Central grow and improve.
            
Pop on over to the Contact tab to reach out: questions, feedback, suggestions,
new data. Would love to hear from you!
""")

# Footer
st.markdown("---")
st.markdown("""
*KHML Central is an independent fan-made project and is not affiliated with the 
official Kingdom Hearts brand or its creators.*
""")
