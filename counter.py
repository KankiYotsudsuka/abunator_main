# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:20:26 2020

@author: School
"""


# coding: utf-8

import sys
sys.path.append("/abunator_main/")

import psycopg2

#これまでのSQL文、カラム、質問を収納します
SQLList = []
ColumnList = []
QuestionList = []

users = "postgres"
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

#DBに接続
def get_connection():
#    return psycopg2.connect(DATABASE_URL)

#サーバーのPostgresにつなぐときは↓
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

#回答をリストに記録
def ListMaker(answer,column,question):
    if answer == 0 :
        Mher = column + " = '" + question + "'"
        SQLList.append(Mher)
    elif answer == 1 :
        Mher = column + " != '" + question + "'"
        SQLList.append(Mher)
    elif answer == 2 :
        Mher = "no >= 1"
        SQLList.append(Mher)

#過去の回答内容を取り出してSQL文にする
def SQLMaker():
    David = "no >= 1"
    for i in range(0,len(SQLList)):
        David = David + " and " + SQLList[i]
    return  David

#回答の内容に合致する動物の数を数える
#def GetCount(answer,column,question):
#        ListMaker(answer,column, question)
def GetCount():
        with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select count (*) from maintable where " + SQLMaker())
                results = cur.fetchall()
        for i in results:
            Ararat = i[0]
            break
        return int(Ararat)