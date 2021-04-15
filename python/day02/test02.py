math=input("수학점수를 입력하시오")
ko=input("국어점수를 입력하시오")
en=input("영어점수를 입력하시오")

sum= int(math)+int(ko)+int(en)
avg= sum/3
print("총점:",sum)
print("평균:",round(avg))
