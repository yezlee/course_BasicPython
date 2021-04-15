import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
curs = conn.cursor() 

sql = "SELECT s_price,in_time FROM stock WHERE s_name = '안국약품' order by in_time DESC"
curs.execute(sql)

rows = curs.fetchall()

prices = []
for row in rows:
    prices.append(row[0])
    

conn.close()
