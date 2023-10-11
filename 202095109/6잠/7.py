'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:Lab 6-4 

[알고리즘]
(함수)
        5)두 값을 전달받아 매개 변수에 저장
        6)최대값,최소값을 찾는다
        7)값을 돌려준다
(메인)
    1.무한반복
        1)런댐으로 10~99까지 10개의 수를 리스트로 생성
        2)생송ㄷ한 라스트를 출력
        3)상용자로부터 최대값을 알고 싶은지 최소값을 알고 싳은지 묻는다.
            사용자가 입력할 값은 max 또는 min
        4)입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
        8)돌려 받은 최대값 또는 최소값을 출력한다
'''
import random as r

def get_MinMax(list,input):
    if input=='max':
        max_num=list[0]
        for i in list:
            if i>max_num:
                max_num=i
        return max_num
    elif input=='min':
        min_num=list[0]
        for i in list:
            if i<min_num:
                min_num=i
        return min_num
    else:print("illegal input")
    print()
    
while(True):
    mList = [r.randint(1, 100) for i in range(10)]
    while(True):
        print(mList)
        mInput=input("enter 'max' or 'min' to sort the list:")
        print(get_MinMax(mList,mInput))