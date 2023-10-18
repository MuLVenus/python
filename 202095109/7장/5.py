'''
작성일:2023년 10월 18일
작성자:202095109 양사호
설명:
'''

fruits1=['strawberry','watermelon','banana']

fruits2=fruits1

print(f"fruits1:{fruits1}")
print(f"fruits2:{fruits2}")

fruits2[1]='mango'
print(f"fruits1:{fruits1}")
print(f"fruits2:{fruits2}")

print(f"fruit1 list's id:{id(fruits1)}")
print(f"fruit2 list's id:{id(fruits2)}")

fruits2=list(fruits1)
print(f"fruits1:{fruits1}")
print(f"fruits2:{fruits2}")

print(f"fruit1 list's id:{id(fruits1)}")
print(f"fruit2 list's id:{id(fruits2)}")

fruits3=fruits1[:]
print(f"fruits1:{fruits1}")
print(f"fruits3:{fruits3}")

print(f"fruit1 list's id:{id(fruits1)}")
print(f"fruit3 list's id:{id(fruits3)}")

fruits3[0]='watermelon'
print("::after fruits3[0] changes to watermelon::")
print(f"fruits1:{fruits1}")
print(f"fruits3:{fruits3}")

print(f"fruit1 list's id:{id(fruits1)}")
print(f"fruit3 list's id:{id(fruits3)}")