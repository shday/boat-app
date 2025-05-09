import random
import time
import streamlit as st
#from openai import OpenAI

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "What's white and falls from the sky?",
            "Hi, human! Let's play a game.",
            "What pops at parties?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Steve's Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    if 'ballon' in prompt:
        st.balloons()

    if 'snow' in prompt:
        st.snow()
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})