from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql
import datetime

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

curs = conn.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php?koskok=KOSDAQ&orderBy=upjong")
 
bsObject = BeautifulSoup(html, "html.parser") 

now = datetime.datetime.now()
in_time = now.strftime('%Y%m%d.%H%M')

tds = bsObject.select(".st2")

for td in tds:
    s_code = td.find(["a"]).get('title')
    s_name = td.text
    s_price = td.parent.select("td")[1].text.replace(",","")
    
    sql = "insert into stock(s_code,s_name,s_price,in_time) values (%s, %s, %s, %s)"
    curs.execute(sql, (s_code, s_name, s_price, in_time))
conn.commit()        
conn.close()
 
    