import pymysql
 
conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
curs = conn.cursor()

sql = "delete from sample where col01=%s"
curs.execute(sql, 1)
 
conn.commit()
conn.close()