def q2():
    import streamlit as st

    placeholder = st.empty()
    answer = placeholder.radio("Question 2", ("Yes", "No"))

    return answer
