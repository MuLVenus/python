'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:함수에 일을 시키고 그값을 받아 오기

원의 넚이 구하기
반지름이 3인 원의 없이를 구한다
반지름 값을 전달받아 원의 넓이를 구하고 얿이를 돌려주는 함수를 작성

[알고리즘]
(함수) area
    1.반지름 값을 전달받아 매개 변수에 저장한다
    2.반지름으로 원의 넓이를 계산한다
    계산된 넓이를 함수를 홏출한 곳으로 돌려준다.
    
(함수 호출하는 메인)
    1.반지름을 가지고 함수를 호출한다
    돌려받은 넓이를 출력한다
'''

def area(radius):
    result=3.14*radius**2
    return result

result=area(3)
print(f"The area of a circle with a radius of 3 is. {result}")
print(f"The area of a circle with a radius of 3 is. {area(3)}")

print()
print("_______________")

r=int(input("enter the radius:"))
print(f"The area of a circle with a radius of {r} is. {area(r)}")