'''
    작성일:2023년 11원 1일
    작성자:양사호
    설명:lab 8-1
'''

items={'커피음료':7,'펜':3,'조잉컵':2,'우유':1,'콜라':4,'책':5}

while(True):
    chioce=input("item name('stop' to stop):")
    for key in items.keys():
        if chioce==key:
            print(f"storage:{items[key]}")
    if chioce=='stop':break