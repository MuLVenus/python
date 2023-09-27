'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:점수를 입력받아 학점을 출력하시오.
    90~100:A학점
    80~89:B학점
    70~79:C학점
    60~69:D학점
    0~59:F학점
'''

score=int(input("score:"))

if(score<=100 and score>=90):print("A")
elif(score <=89 and score>=80):print("B")
elif(score <=79 and score>=70):print("C")
elif(score <=69 and score>=60):print("D")
elif(score <=59 and score >=0):print("F")
else:print("unkown score")

if(0<score<=100):
        if(90<=score<=100):print("A")
        elif(80<=score<=89):print("B")
        elif(70<=score<=79):print("C")
        elif(60<=score<=69):print("D")
        else:print("F")
else:print("unkown score")