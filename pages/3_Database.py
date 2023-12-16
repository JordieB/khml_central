import pandas as pd
import streamlit as st

st.title("Database")

# Init db connection
conn = st.connection('db', type='sql')

df = conn.query('SELECT * FROM ttpi WHERE flag = :flag',
                params={'flag': True})
st.dataframe(df)
