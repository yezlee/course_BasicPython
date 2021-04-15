import pymysql
 
conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
 
curs = conn.cursor()
sql = """insert into sample(col01,col02,col03)
         values (%s, %s, %s)"""
curs.execute(sql, (10, 11, 12))
conn.commit()
 
conn.close()