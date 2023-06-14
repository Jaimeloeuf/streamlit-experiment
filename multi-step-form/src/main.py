def main():
    import streamlit as st
    from menu import menu
    from question_number import get_question_number, increment_question_number

    menu()

    match get_question_number():
        case 1:
            from questions.q0 import q0, invalid_q0
            from questions.q1 import q1

            st.session_state["q0_answer"] = q0()
            st.session_state["q1_answer"] = q1()

            def validate_answers():
                if invalid_q0(st.session_state["q0_answer"]):
                    return

                # Only go to next question if there are no more errors!
                increment_question_number()

            st.button("Next", on_click=validate_answers)

        case 2:
            from questions.q2 import q2

            st.session_state["q2_answer"] = q2()

            st.button("Next", on_click=increment_question_number)

        # This is not a question, this is the "final page"
        case 3:
            st.header("Here are your answers from previous questions")
            st.write(st.session_state["q0_answer"])
            st.write(st.session_state["q1_answer"])
            st.write(st.session_state["q2_answer"])

        case _:
            st.error("Invalid question number!")


main()
