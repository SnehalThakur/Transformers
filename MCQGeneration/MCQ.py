import streamlit as st
import utils.SQLiteDBOps as db
import numpy as np
import pandas as pd
import ast

mcqData = db.retrieveMCQDataWithTopic('data science')
mcqList = []
for mcq in mcqData:
    mcqDict = {}
    # print(mcq)
    id = mcq['id']
    # print("id =", id)
    question = mcq['question']
    # print("question =", question)
    options = list(ast.literal_eval(mcq['options']))
    options.insert(0, "None")
    # print("options =", options)
    # print("type(options) =", type(options))
    answer = mcq['answer']
    # print("answer =", answer)
    topic = mcq['topic']
    # print("topic =", topic)
    difficulty = mcq['difficulty']
    # print("difficulty =", difficulty)
    mcqDict["question"+" "+str(id)] = question
    mcqDict["correctAnswer"] = answer
    # print("-------------")
    que = st.subheader(str(id)+" "+question)
    # arr = pd.Series(options)
    status = st.radio("Select Correct Option: ", options)
    mcqDict["choosenAnswer"] = status

    mcqList.append(mcqDict)
    # mcqDict.clear()

# print("mcqList =", mcqList)
if st.button("submit"):
    st.header("===== Solution ======")
    for mcq in mcqList:
        question = ""
        answer = ""
        status = ""
        for key, val in mcq.items():
            status = mcq["choosenAnswer"]
            if key.startswith("question"):
                question = mcq[key]
            answer = mcq["correctAnswer"]
        st.subheader(question)
        if status == answer:
            st.write("Correct Answer")
            st.success(answer)
        else:
            st.write("Your Answer")
            st.error(status)
            st.write("Correct Answer")
            st.success(answer)
