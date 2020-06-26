import psycopg2

def get_connection():
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

def result():
    with get_connection() as conn:
        with conn.cursor() as cur:
            #SQL文実行
            cur.execute('select * from maintable where no = 2')
            results = cur.fetchall()
    for i in results:
        no = str(i[0])
        name = str(i[1])
        dealing = str(i[17])
        rank = str(i[18])
        resultList = [no,name,dealing,rank]
        break
    return resultList

result = result()
print(result)