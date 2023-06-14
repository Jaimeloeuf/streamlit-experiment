def q0():
    import streamlit as st

    placeholder = st.empty()
    answer = placeholder.text_input("What is your name?")
    return answer
