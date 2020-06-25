# coding: utf-8

import psycopg2
import random
import counter
import sys
sys.path.append("/abunator_main/")

#host = "18.181.156.243"
#port = "5432"
#dbname = "abunator"
#user = "postgres"
#password = "Ag9e832p@_30g!3d0b8alvm20;"
#table = "animals"
#DATABASE_URL = "host=" + user + "port=" + port + "dbname=" + dbname + "user=" + user + "password=" + password
#サーバー上のDBにつなぐときは↑



users = "Postgres"
dbnames = "Abunator"
passwords = "postgres"
table = "maintable"

global num
num = 0
#DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords
#ローカルのDBにつなぐときは↑

#culumnList = ["size","division","color","region","place","time","season","poison","pattern","symptoms","food","sucker","epidemic","foreigner","individuality"]
questionList = ["在来種","伝染病を媒介する可能性は低い","ヒトから吸血しない","特徴的な模様を持っていない","夜行性","毒を持つ","全国に生息する","一年を通して活動する","海中に住む","昆虫類","他の動物や植物を食べる","体色は「茶色」","体長は約「10cm」","激しい痛みを起こし、刺された箇所が赤く腫れる","多くのトゲを背中に持ち、胸びれは扇のような形をしている"]
culumnList = ["foreigner","epidemic","sucker","pattern","time","poison","region","season","place","division","food","color","size","symptoms","individuality"]
suspendedCList = ["pattern","region","season","place","division","food","color","size","symptoms","individuality"]

def setQuestion():
    questionList.clear

def get_connection():
#    return psycopg2.connect(DATABASE_URL)
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")


def getCulumn():
    if (len(counter.QuestionList) <= 35 and len(counter.QuestionList) >= 15):
        num = random.randint(0,len(suspendedCList)-1)
        culumn = suspendedCList[num]
#        counter.ColumnList.append(culumn)
        return culumn
    
    elif(len(counter.QuestionList) < 15):
        num = len(counter.QuestionList)
        culumn = culumnList[num]
#        counter.ColumnList.append(culumn)
        return culumn

    elif(len(counter.QuestionList) > 35):
        culumn = "individuality"
        return culumn

def getQuestion(culumn):
    if len(counter.QuestionList) < 14:
        question = questionVerse(culumn)
#        counter.QuestionList.append(question)
#        return 'それは'+ str(question) + '？'
        return question
    
    else:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT " + culumn + " FROM maintable ORDER BY random() limit 1")
                results = cur.fetchall()
                for i in results:
                    question = i[0]
                    break
#                counter.QuestionList.append(question)
#                return 'それは'+ str(question) + '？'
                return question

def questionVerse (calm):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT "+ calm +", count("+ calm +") AS COUNT FROM maintable GROUP BY "+ calm +" ORDER BY COUNT desc;")
            results = cur.fetchall()
    for i in results:
        question=i[0]
        break
#    counter.QuestionList.append(question)
    return question