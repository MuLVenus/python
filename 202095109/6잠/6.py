'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:함수의 디폴트 인자
'''

def order1(num,pickle,onion):
    print(f'햄버거 {num} -피클 {pickle} ,양파 {onion}')

def order2(num,pickle="기본",onion="기본"):
    print(f'햄버거 {num} -피클 {pickle} ,양파 {onion}')
    
order2(1)
order2(1,pickle="뱀",onion="기본")