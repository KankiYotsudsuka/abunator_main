import pytest
import psycopg2
import counter  # テスト対象のモジュールをインポートする


def test_counter():
    counter.ListMaker(0,'foreigner','在来種')
    amount = counter.GetCount()
    answer = int(TotalCount()) 
    # 関数の返り値が期待した内容と一致するか確認する
    assert amount == answer-2

def get_connection():
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

def TotalCount():
        with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select count (*) from maintable ")
                results = cur.fetchall()
        for i in results:
            Maya = i[0]
            break
        return int(Maya)
