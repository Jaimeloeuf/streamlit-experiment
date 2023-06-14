def set_default_if_none():
    import streamlit as st

    # Check if 'current_question_number' already exists in session_state
    # If not, then initialize it
    if "current_question_number" not in st.session_state:
        st.session_state.current_question_number = 1


def get_question_number():
    import streamlit as st

    set_default_if_none()

    return st.session_state.current_question_number


def increment_question_number():
    import streamlit as st

    set_default_if_none()

    st.session_state.current_question_number += 1
