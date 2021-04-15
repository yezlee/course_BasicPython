import pymysql
import time
 
conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
 
curs = conn.cursor()

start = time.time()

for i in range(300000):
    sql = """insert into sample(col01,col02,col03)
         values (%s, %s, %s)"""
         
    curs.execute(sql, (i, i, i))
conn.commit()
 
print("time : ", time.time()-start)
conn.close()