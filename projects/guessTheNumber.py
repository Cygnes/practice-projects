import random

print("Guess The Number Game!!")

# 5 tries to guess the number
for i in range(5):
    number = int(random.randrange(1, 21))
    user = int(input("Enter Number Here:"))
    if user == number:
        print("You Won!!")
        break
    elif number > 10:
        print("Number is greater than 10, try again!!")
    elif number < 10:
        print("Number is lesser than 10, try again!!")