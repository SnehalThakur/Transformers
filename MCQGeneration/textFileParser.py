from utils import SQLiteDBOps

# text = """
# 1. What is the most popular programming language used for data science?
# A. Python
# B. Java
# C. C++
# D. R
# Answer: A. Python
#
# 2. What is the main purpose of data science?
# A. To help businesses make decisions
# B. To develop software
# C. To analyze data
# D. To create websites
# Answer: C. To analyze data
#
# 3. What type of data is most commonly used in data science?
# A. Text
# B. Images
# C. Audio
# D. Structured
# Answer: D. Structured
#
# 4. What is the most important skill for a data scientist?
# A. Mathematics
# B. Programming
# C. Communication
# D. Machine Learning
# Answer: B. Programming
#
# 5. What is the first step in the data science process?
# A. Collecting data
# B. Analyzing data
# C. Visualizing data
# D. Cleaning data
# Answer: A. Collecting data
# gptResponse
#
# 1. What is the most popular programming language used for data science?
# A. Python
# B. Java
# C. C++
# D. R
# Answer: A. Python
#
# 2. What is the main purpose of data science?
# A. To help businesses make decisions
# B. To develop software
# C. To analyze data
# D. To create websites
# Answer: C. To analyze data
#
# 3. What type of data is most commonly used in data science?
# A. Text
# B. Images
# C. Audio
# D. Structured
# Answer: D. Structured
#
# 4. What is the most important skill for a data scientist?
# A. Mathematics
# B. Programming
# C. Communication
# D. Machine Learning
# Answer: B. Programming
#
# 5. What is the first step in the data science process?
# A. Collecting data
# B. Analyzing data
# C. Visualizing data
# D. Cleaning data
# Answer: A. Collecting data
# """


def gptResponseParser(gptResponse, topic, level):
    textList = gptResponse.strip().split("\n\n")

    questionList = []
    answersList = []
    for txt in textList:
        text = txt.strip().split('\n')
        question = str(text[0][3:]).strip()
        correctAnswer = str(text[-1][7:]).strip()
        options = str(text[1:-1]).strip()

        SQLiteDBOps.insertMCQData(question, str(options), correctAnswer, topic, level)

        print("question =", question)
        print("correctAnswer =", correctAnswer)
        print("options =", options)
        print("----------------------------")
    mcqResponse = SQLiteDBOps.retrieveMCQData()
    print("mcqResponse =", mcqResponse)
