import random

subtractNumber = random.randrange(5)

print("__________________________") #25
print("|  The Wrong Calculator  |") 
print("|________________________|")

print("(This is a WIP - work in progress. so there is only addition working)")
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

product = number1 + number2
answer = product - subtractNumber

print(answer)
