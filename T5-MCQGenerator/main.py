import textwrap
import streamlit as st
from app.mcq_generation import MCQGenerator
import SQLiteDB as dbHandler


def show_result(generated: str, answer: str, context: str, original_question: str = ''):
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

st.title("MCQ generation using NLP")

if 'num' not in st.session_state:
    st.session_state.num = 0

choices1 = ['no answer', 'manila', 'tokyo', 'bangkok']
choices2 = ['no answer', 'thailand', 'japan', 'philippines']

qs1 = [('What is the capital of Japan', choices1),
       ('What is the capital of Philippines', choices1),
       ('What is the capital of Thailand', choices1)]
qs2 = [('What country has the highest life expectancy?', choices2),
       ('What country has the highest population?', choices2),
       ('What country has the highest oil deposits?', choices2)]


def main():
    topic = st.selectbox("Select the topic for MCQ Generation: ",
                         ['PYTHON', 'HTML', 'CSS', 'DataStructures', 'CPP'])

    # print the selected topic
    # st.write("Your topic is: ", topic)
    retrivedDataFromDB = dbHandler.retrieveCorpusDataWithItemName(topic)[0][2]
    # print(dbHandler.retrieveCorpusDataWithItemName(topic))
    if st.button("Generate"):
        st.text_area(label=topic, value=retrivedDataFromDB, height=700)

        questions = MCQ_Generator.generate_mcq_questions(retrivedDataFromDB, 10)
        print("MCQ =", questions)

        answers = []
        for question in questions:
            if question.answerText:
                print('-------------------')
                print(question.questionText)
                st.text(question.questionText)
                answers.append(question.answerText)
                st.success(question.answerText)
                print(question.answerText)
                for ans in question.distractors:
                    st.error(ans)
                print(question.distractors)
                answers.append(question.distractors)
                st.write('\n')
                st.write('\n')
                st.write('\n')

    # for _, _ in zip(qs1, qs2):
    #     placeholder = st.empty()
    #     num = st.session_state.num
    #     with placeholder.form(key=str(num)):
    #         st.radio(qs1[num][0], key=num + 1, options=qs1[num][1])
    #         st.radio(qs2[num][0], key=num + 1, options=qs2[num][1])
    #
    #         if st.form_submit_button():
    #             st.session_state.num += 1
    #             if st.session_state.num >= 3:
    #                 st.session_state.num = 0
    #             placeholder.empty()
    #         else:
    #             st.stop()


main()

# with st.form("my_form"):
#    st.write("Inside the form")
#    slider_val = st.slider("Form slider")
#    checkbox_val = st.checkbox("Form checkbox")
#
#    # Every form must have a submit button.
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#        st.write("slider", slider_val, "checkbox", checkbox_val)
#
# st.write("Outside the form")

#
# for question in questions:
#     print('-------------------')
#     print(question.answerText)
#     print(question.questionText)
#     print(question.distractors)
