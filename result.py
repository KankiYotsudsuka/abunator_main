# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:36:33 2020

@author: School
"""
import sys
sys.path.append("/abunator_main/")
import counter
import psycopg2


users = "postgres"
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

def get_connection():
#    return psycopg2.connect(DATABASE_URL)

    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

def resNumber():
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select no from maintable where " + counter.SQLMaker())
                results = cur.fetchall()
    for i in results:
        Aramazd = i[0]
        break
    return int(Aramazd)

def resName(number):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select name from maintable where no = " + str(number))
                results = cur.fetchall()
    for i in results:
        Anahit = i[0]
        break
    return str(Anahit)

def resDealing(number):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select dealing from maintable where no = " + str(number))
                results = cur.fetchall()
    for i in results:
        Vahagn = i[0]
        break
    return str(Vahagn)

def resRank(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select danger from maintable where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        mihr = i[0]
        break
    return str(mihr)

#変数としてresNumberの結果を記録し、それを鍵として、動物の名前と画像とコメントを取り出す

def insert(no,name):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("delete from record where no = " + no + "; insert into record(no,name) values(" + no + ", '" + name + "');")
#                cur.execute("insert into record values(" + no + ",'" + name + "')")

#今回の結果はDBに記録され、次にアプリを起動した場合に「前回の結果」として表示される

def result():
    with get_connection() as conn:
        with conn.cursor() as cur:
            #SQL文実行
            cur.execute('select * from maintable where ' + counter.SQLMaker())
            results = cur.fetchall()
    for i in results:
        no = str(i[0])
        name = str(i[1])
        dealing = str(i[17])
        rank = str(i[18])
        resultList = [no,name,dealing,rank]
        break
    return resultList