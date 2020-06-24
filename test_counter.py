import unittest
import psycopg2
import counter  # テスト対象のモジュールをインポートする


class test_counter(unittest.TestCase):
    """helloworld モジュールのテストを記述するクラス"""

    def test_greet(self):
        counter.ListMaker(0,'foreigner','在来種')
        amount = counter.GetCount()
        answer = int(TotalCount()) 
        # 関数の返り値が期待した内容と一致するか確認する
        self.assertEqual(amount, answer-2)

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


if __name__ == '__main__':
    # スクリプトとして実行された場合の処理
    unittest.main(verbosity=2)