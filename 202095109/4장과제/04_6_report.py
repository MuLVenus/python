print("welcome,this is the menu")
print("---->Hamburger (letter:b)")
print("---->Chicken (letter:c)")
print("---->Pizza (letter:p)")

letter=input("which menu will you choose(please enter b,c,or p):")

if letter=="c" or letter=="C":print("yes, you choose the chicken")
elif letter=="b" or letter=="B":print("yes, you choose the Hamburger")
elif letter=="p" or letter=="P":print("yes, you choose the pizza")
else:print("sorry,the menu hasn't find, please try it again")