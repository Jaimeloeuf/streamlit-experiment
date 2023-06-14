def q1():
    import streamlit as st

    placeholder = st.empty()
    answer = placeholder.radio("Question 1", ("Yes", "No"))

    return answer
