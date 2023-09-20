'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:선탣문 if-else
    정수를 입력받아 짝수인지 폴수인지 판단.
    짝수,홀수는 양수일 경우에만 판단한다.
    
    짝수=2로 나눈 나머지가 0이다.
    홀수=2로 나눈 나머지가 1이다.(0이 아니다.)
'''

num=int(input("정수 입력하시오:"))

if num<0:
    print(num,"은/는 음수입니다")
    print("{}은/는 음수입니다".format(num))
    print(f"{num}은/는 음수입니다")
else:
    print(num,"은/는 양수입니다")
    print("{}은/는 양수입니다".format(num))
    print(f"{num}은/는 양수입니다")
    if num%2==0:
        print(num,"은/는 짝수입니다")
        print("{}은/는 짝수입니다".format(num))
        print(f"{num}은/는 짝수입니다")
    else:
        print(num,"은/는 홀수입니다")
        print("{}은/는 홀수입니다".format(num))
        print(f"{num}은/는 홀수입니다")