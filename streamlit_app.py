import streamlit as st
from datetime import datetime

#date = st.date_input("Date?",format="DD-MM-YYYY")
if not st.session_state.get('go'):
    st.markdown(f"## {datetime.now()}")

x = st.multiselect("choose",['a','b','c'],)

if st.button("Go!",key='go'):
    st.write(str(x))

