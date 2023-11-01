'''
    작성일:2023년 11원 1일
    작성자:양사호
    설명:한번 생성하면 그값을 고칠 수 없는 자료형 :튜플
'''

color_list=["red","green",'blue',"orange"]

color=["red","green",'blue',"orange"]

print(f"color:{color}")

#color.append("black")

print(f"color 튜플:{color}")
print(f"color 튜플 중 2,3,4번은? {color[1:4]}")
print(f"color 튜플 중 1,2,3번은? {color[:3]}")
print(f"color 튜플 중 1,3,5번은? {color[::2]}")
print(f"color 튜플 중 3번-끝? {color[2:]}")
print(f"color 튜플 중 거꾸로 출력? {color[::-1]}")

colors=color*10
print(f"colors:{colors}")
print(f"color*10:{color*10}")