import streamlit as st


st.title("🎈 My new apple")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

date = st.date_input("Date?",format="DD-MM-YYYY")

st.write(date.strftime("%d-%b-%Y"))

x = st.multiselect("choose",['a','b','c'],)

st.write(x)
