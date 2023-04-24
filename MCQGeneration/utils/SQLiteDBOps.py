import sqlite3 as sql


def createMCQTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\MCQGeneration\utils\SQLiteDB\MCQData.db")
    print(sqlConnection)

    sqlConnection.execute("""
            CREATE TABLE IF NOT EXISTS mcq (
                id integer primary key autoincrement,
                question text not null,
                options text not null,
                answer text not null,
                topic text not null,
                difficulty text not null
                );
        """)


def insertMCQData(question, option, correctans, topic, level):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\MCQGeneration\utils\SQLiteDB\MCQData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO mcq (question, options, answer, topic, difficulty) VALUES (?,?,?,?,?)",
                (question, option, correctans, topic, level))
    con.commit()
    con.close()


def retrieveMCQData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\MCQGeneration\utils\SQLiteDB\MCQData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM mcq")
    mcqData = cur.fetchall()
    mcqData_accumulator = []
    for mcq in mcqData:
        mcqDataDict = {"id": mcq[0], "question": mcq[1], "options": mcq[2], "answer": mcq[3], "topic": mcq[4], "difficulty": mcq[5]}
        mcqData_accumulator.append(mcqDataDict)
    # print("mcqData =", mcqData_accumulator)
    con.close()
    return mcqData_accumulator


def retrieveMCQDataWithTopic(topicName):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\MCQGeneration\utils\SQLiteDB\MCQData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM mcq where topic='{topicName}'")
    mcqData = cur.fetchall()
    mcqData_accumulator = []
    for mcq in mcqData:
        mcqDataDict = {"id": mcq[0], "question": mcq[1], "options": mcq[2], "answer": mcq[3], "topic": mcq[4], "difficulty": mcq[5]}
        mcqData_accumulator.append(mcqDataDict)
    # print("mcqData =", mcqData_accumulator)
    con.close()
    return mcqData_accumulator


# createMCQTableIfNotExist()
# retrieveMCQData()
retrieveMCQDataWithTopic("data science")
