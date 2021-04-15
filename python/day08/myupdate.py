import pymysql
 
conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
curs = conn.cursor()

sql = """update sample
         set col01=%s,col02=%s,col03=%s 
         where col01 = '5' and col02='6' and col03='9'"""
curs.execute(sql,(4,4,4))
 
conn.commit()
conn.close()

