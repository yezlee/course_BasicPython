from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
 
bsObject = BeautifulSoup(html, "html.parser") 

tds = bsObject.select(".st2")
 
for td in tds:
    s_code = td.find(["a"]).get('title')
    s_name = td.text
    s_price = td.parent.select("td")[1].text
    print("s_code:",s_code, end=' ')
    print("s_name:",s_name, end=' ')
    print("s_price:",s_price)
 
        
    