'''
작성일:20203년 11월 8일
작성자:양사호 202095109
설명:집합 set()
'''

number=set()

number1=(2,1,3)
print(f"집합 number1:{number1}")
print()

number2=set([1,2,3,4,5])
print(f"집합 number2:{number2}")
print()

test1=set("asdfghjkl")
print(f"집합 test1:{test1}")
print()

numbers={2,4,5,1,2}
if 1 in numbers:print("one is here")
print()

numbers={9,1,8,2,7,3,4,5,6}
for num in numbers:
    print(num,end='')
print()

for num in sorted(numbers):
    print(num,end='')
print()

for num in sorted(test1):
    print(num,end='')
print()

numbers.add(100)
print(numbers)
for num in sorted(numbers):
    print(num,end='')
print()

numbers.remove(100)
print(numbers)
