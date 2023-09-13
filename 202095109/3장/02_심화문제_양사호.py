'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:90페이지 문제 3.9
    핑균 시속과 이동시간을 입력받아
    이동 시간은 시, 분,초 단위로 출력하고,
    이동한 거리를 계산 하여 출력하시오.

'''

speed=float(input("the average speed is "))
time=float(input("the time spend in the moving is "))

hours = int(time)
minutes = int((time - hours) * 60)
seconds = int(((time - hours) * 60 - minutes) * 60)

print("average speed:{}km/h".format(speed))
print("travel time:{}hour {}minute {}second".format(hours,minutes,seconds))
print("total distance:{}km".format(speed*time))