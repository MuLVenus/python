'''
작성일:2023년 9월 27일
작성자:202095109 양사호
설명:반복문 for 사용하기
'''
for i in range(5):
    print(i+1,"양사호")

print()

for i in [1,2,3,4,5]:
    print(i,"양사호")
    
print()

for i in range(9):
    print(f"{i+1}*19={(i+1)*19}")
    
print()
for i in range(1,10):
    print(f"{i}*19={i*19}")
    
print()
for i in"HELLO":
    print(f"{i}")

print()
BTS=["뷔","제이홉","알엠","정국","진","지민","슈가"]
for i in range(len(BTS)):
    print(f"{i+1}:{BTS[i]}")