import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"대전맛집"}
header = {'authorization':'KakaoAK 8c95c582f0b5a96e302f96c9a6ba1877'}
r = requests.get(url, headers=header, params=queryString)
for i in r.json()["documents"]:
    print(i["cafename"])
    print(i["contents"])
    print(i["datetime"])
    print(i["thumbnail"])
    print(i["title"])
    print(i["url"])
