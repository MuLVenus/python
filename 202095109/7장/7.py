'''
    작성일:2023년 11원 1일
    작성자:양사호
    설명:LAB 7-5 함수는 튜플을 돌려줄 수있다
    
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오
        넓이와 둘레를 계산하는 함수를 작성하시오
        함수는 업ㄹ이와 둘레를 함께돌려줍니다.
        
        [함수]
        3.반지름을 받아서 매개변수에 저장한다
        4.얿이와 둘레를 계산한다
        5.얿이와 둘레를 돌려준다.(함수를 호출한 곳으로) return 넓이,둘레

        [메인]
        1.빈지름을 입력 받는다
        2.함수 호툴->반지름을 가지고 호출한다
        6.돌려받은업ㄹ이와 둘레를 튜플로 저장한다.(넓이,둘레)
        7.출력한다
'''

def circle(radius):
    pi=3.1415926
    area=radius**2*pi
    circum=radius*2*pi
    return area,circum

while(True):
    radius=int(input("enter the radius of a circle(enter 0 to stop):"))
    if(radius==0): break;
    (a,c)=circle(radius)    
    print(f"area:{a:.2f},circum:{c:.2f}")