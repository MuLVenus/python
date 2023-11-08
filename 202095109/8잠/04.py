'''
작성일:20203년 11월 8일
작성자:양사호 202095109
설명:집합 set()
'''

num1={1,2,3}
num2={1,2,3}
print(f"num1==num2? {num1==num2}")

num_set={1,4,5,6,3,5}
print(f"num_set:{num_set}")
print(f"num_set 길이: {len(num_set)}")
print(f"num_set 중 가장 콘 값:{max(num_set)}")
print(f"num_set 중 가장 작은 값:{min(num_set)}")
print(f"num_set 합게:{sum(num_set)}")
print()

num1={1,2,3}
num2={3,4,5}
print(f"num1|num2:{num1|num2}")
print(f"num1.union(num2):{num1.union(num2)}")
print(f"num1^num2:{num1^num2}")