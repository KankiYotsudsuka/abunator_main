# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:20:15 2020

@author: School
"""
# coding: utf-8

#todo
#データベース読み込み
#ランダムに生物名選択
#選択肢ランダム選択
#選択肢減らして探索
#そこまでの選択肢保存

import psycopg2
import random

import sys
sys.path.append("/abunator_main/")

import counter

baseList = ['no','name','division','size','color','region','place','time','pattern','poison','symptoms','food','sucker','epidemic','foreigner','season','individuality','dealing']

users = "postgres"
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
#DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords


#DBに接続
def get_connection():
#    return psycopg2.connect(DATABASE_URL)

#サーバーのpostresにつなぐときは↓
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")


#DBのnameカラムからランダムに選択
def randomName():
    num=random.randint(1,40)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM creatures WHERE num='"+str(num)+"';")
            results = cur.fetchall()
            print(results)



#ここから下はJavaの関数と同じ動き

def getMaxCalm(calm):
    #withで書くことで勝手にclose()とかしてくれる
    with get_connection() as conn:
        with conn.cursor() as cur:
            #SQL文実行
            cur.execute("SELECT "+ str(calm) +", count("+ str(calm) +") AS COUNT FROM maintable GROUP BY "+ str(calm) +" ORDER BY COUNT desc;")
            results = cur.fetchall()
    #この場合、情報は[(uuu, nnn), (ccc, hhh), ・・・, (iii, ooo)]の形でresultsに格納されている
    #今欲しいのはnnnの部分のため、for文でそこだけ取り出す
    for i in results:
        number=i[1]
        break

    return int(number)

def questionVerse (calm):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT "+ calm +", count("+ calm +") AS COUNT FROM maintable GROUP BY "+ calm +" ORDER BY COUNT desc;")
            results = cur.fetchall()
    for i in results:
        question=i[0]
        break

    counter.QuestionList.append(question)
    return "それは"+question+"？"

def getCalm(list):
    MAX=0
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM maintable;")
            results = cur.fetchall()
#    for i in results:
#        if not(list in i[0]):
#        if not(i[0] in list):
#            if(MAX<getMaxCalm(i[0])):
#                MAX=getMaxCalm(i[0])
#                buriburi= i[0]

    for i in range(0,len(baseList)-1):
        if not(baseList[i] in list):
            if(MAX<getMaxCalm(baseList[i])):
                MAX=getMaxCalm(baseList[i])
                buriburi= baseList[i]

    counter.ColumnList.append(buriburi)
    return buriburi



#print(questionVerse("division"))