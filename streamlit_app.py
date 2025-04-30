import streamlit as st
from datetime import datetime

cols = st.columns(2)
#date = st.date_input("Date?",format="DD-MM-YYYY")
if not st.session_state.get('go'):
    cols[0].markdown(f"## {datetime.now()}")

x = cols[1].multiselect("choose",['a','b','c'],)

if cols[1].button("Go!",key='go'):
    st.write(str(x))

