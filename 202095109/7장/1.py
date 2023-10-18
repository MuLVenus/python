'''
작성일:2023년 10월 18일
작성자:202095109 양사호
설명:리스트 만들기
'''

fruits=['strawberry','apple','banana']
print("fruit list:",fruits)
print()

fruits.append('watermelon')
print("fruit list (add watermelon):",fruits)
fruits.append('mango')
print("fruit list(add mango):",fruits)
print()

fruits=fruits+['grape']
print("fruit list(add grape):",fruits)

num=[1,2,3]+[4,5,6]
print("number list:",num)
print()

num=[1,2,3]*3
print("number list *3:",num)

print("is the mango in the fruit list? ",'mango' in fruits)

'''
178
'''
print("how many fruit in the fruit list?",len(fruits))

print("what is your favorite fruit?",fruits[0])

print("which fruit in the end of fruit list?",fruits[len(fruits)-1])
print("which fruit in the end of fruit list?",fruits[-1])

print("the biggest fruit is",max(fruits))
print("the smallest fruit is",min(fruits))

fruits.sort()
print("sort fruit:",fruits)
fruits.sort(reverse=True)
print("re-sort fruit:",fruits)

'''
리스트를 원하는 모양으로 자르는 슬라이싱
'''

print("fruit list:",fruits)
print("fruit list but from 2 to 4 only:",fruits[1:4])
print("fruit list but from 1 to 3 only:",fruits[0:3])
print("fruit list but from 1 to 3 only:",fruits[:3])
print("fruit list but from 3 to the last only:",fruits[2:])
print("fruit list but 1,3,5 only:",fruits[::2])
print("fruit list:",fruits[::-1])

'''
리스트의 원소 값을 자유롭게 조작해 보자
'''
print()
print("fruit list:",fruits)

fruits.insert(3,'durio')
print("fruit list(list3 add durio)",fruits)

print("the address of apple:",fruits.index('apple'))

fruits.append('apple')
print("fruits list(with addition apple):",fruits)

print("how many apples:",fruits.count('apple'))

'''
delect
'''
print()
fruits.remove('apple')
print("fruit list(after remove apple):",fruits)

fruits.pop()
print("fruit list:",fruits)

del fruits[0]
print("fruit list:",fruits)