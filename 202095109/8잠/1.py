'''
    작성일:2023년 11원 1일
    작성자:양사호
    설명:8.1키와 값을 가지는 딕겨너리
'''

phone_book1={}

phone_book1["양사호"]='202095109'
print(phone_book1)

phone_book2={'양사호':'202095109','KOPL':'202310010'}
print(phone_book2)

phone_book3={}
phone_book3['양사호']='202095109'
phone_book3['KOPL']='202310010'
phone_book3['NOTHI']='202310011'
phone_book3['CERES']='202310012'
phone_book3['LUNA']='202310013'
print(phone_book3)
print(phone_book3.keys())
print(phone_book3.values())
print(phone_book3.items())
print()

for  name,id in phone_book3.items():
    print(f"{name}:{id}")
print()

for key in phone_book3.keys():
    print(f"{key}:{phone_book3[key]}")
print()

person_dict={"name":"Yang SiHao","age":23,"class":"4학년"}
print(f"name:{person_dict['name']}")
print(f"age:{person_dict['age']}")
print(f"class:{person_dict['class']}")
print()

print(sorted(phone_book3))
sort_phone_book3=sorted(phone_book3.items(),key=lambda x:x[0])
print(sort_phone_book3)

sort_phone_book3=sorted(phone_book3.items(),key=lambda x:x[1])
print(sort_phone_book3)
print()

del phone_book3['양사호']
print(phone_book3)

phone_book3.clear()
print(phone_book3)