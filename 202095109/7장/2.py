'''
작성일:2023년 10월 18일
작성자:202095109 양사호
설명:입력을 받아 맛있는 과일의 리스트를 만들자

좋아하는 과일 5개를 입력받아 리스트에 저장한다
과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 찬단한다

추가=append() 메소드
찾기 =in 연사자
'''

fruits=[]
for i in range(5):
    name=input(f"{i+1}.what is your favorite fruit?")
    fruits.append(name)
while(True):
    name=input("enter a fruit name I will check is it your favorite:")
    if(name in fruits):print(f"{name} is your favorite fruit")
    else:print(f"{name} is not your favorite")