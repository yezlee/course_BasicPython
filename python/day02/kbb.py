import random

user = input("가위 바위 보를 선택하세요")
print(user)

com = ""
rnd = random.random()
if rnd > 0.3 :
    com ="가위"
elif rnd > 0.6:
    com="바위"
else :
    com="보"
result=""
if user == com:
    result = "비겼습니다"
elif user > com:
    result ="졌습니다"
else:
    result="이겼습니다"
    
print("com :",com)
print("user :",user)
print("result :",result)