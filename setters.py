# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:50:58 2020

@author: School
"""
import sys
sys.path.append("/abunator_main/")

import counter
import app
import psycopg2

def get_connection():
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")


#ここにある関数を使って、配列と前回の結果を記録したテーブルを初期化できる

def setPathList():
    app.PathList.clear()
    app.PathList.append(0)

def setColumnList():
    counter.ColumnList.clear()
    counter.ColumnList.append("no")
    counter.ColumnList.append("name")
    counter.ColumnList.append("dealing")
    counter.ColumnList.append("danger")

def setQuestionList():
    counter.QuestionList.clear()

def setSQLList():
    counter.SQLList.clear()
    counter.SQLList.append("no >= 1")
