import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
curs = conn.cursor() 

sql = "SELECT * FROM sample"
curs.execute(sql)

rows = curs.fetchall()

print(rows)

conn.close()
