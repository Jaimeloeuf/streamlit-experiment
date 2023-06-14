def q0():
    import streamlit as st

    placeholder = st.empty()
    answer = placeholder.text_input("What is your name?")
    return answer


def invalid_q0(q0_answer):
    import streamlit as st

    # Dont continue if user did not type in a valid name
    if q0_answer == "":
        st.error("Invalid name")
        return True
    else:
        return False
