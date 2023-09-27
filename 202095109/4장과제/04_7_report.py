import random as r

num1=r.randint(1,100)
num2=r.randint(1,100)
sum=num1+num2

answer=int(input(f"{num1}+{num2}="))
if answer==sum:print("Congratulation!")
else:print(f"Sorry, the answer is {sum}")