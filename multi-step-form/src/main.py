def main():
    import streamlit as st
    from menu import menu
    from question_number import get_question_number, increment_question_number

    menu()

    match get_question_number():
        case 1:
            from questions.q0 import q0

            st.session_state["q0_answer"] = q0()

            st.button("Next", on_click=increment_question_number)

        case 2:
            st.button("Next", on_click=increment_question_number)

        # This is not a question, this is the "final page"
        case 3:
            st.header("Here are your answers from previous questions")
            st.write(st.session_state["q0_answer"])

        case _:
            st.error("Invalid question number!")


main()
