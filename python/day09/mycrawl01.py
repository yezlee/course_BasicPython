import urllib.request
from bs4 import BeautifulSoup
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.42.59:8081/HELLOWEB2/crawl.jsp")
 
bsObject = BeautifulSoup(html, "html.parser") 

for td_text in bsObject.find_all("td"):
        print(td_text.getText())
        
    