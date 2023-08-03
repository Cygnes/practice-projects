import random

# TODO: refactor code using functions
# TODO: improve code quality

decision_set = ['rock', 'paper', 'scissors']
win, loss, tie = 0, 0, 0


print("Rock, Paper Scissors Game!!!!!")

for i in range(5):
    user = input("Input here: ")
    computer = random.choice(decision_set)

    if user == 'rock' and computer == 'rock':
        tie += 1
        print("Its A Tie!")
    elif user == 'rock' and computer == 'paper':
        loss += 1
        print("You Lose!")
    elif user == 'rock' and computer == 'scissors':
        win += 1
        print("You Win!")
    elif user == 'paper' and computer == 'paper':
        tie += 1
        print("Its A Tie!")
    elif user == 'paper' and computer == 'rock':
        win += 1
        print("You Win!")
    elif user == 'paper' and computer == 'scissors':
        loss += 1
        print("You Lose!")
    elif user == 'scissors' and computer == 'scissors':
        tie += 1
        print("Its A Tie!")
    elif user == 'scissors' and computer == 'rock':
        loss += 1
        print("You Lose!")
    elif user == 'scissors' and computer == 'paper':
        win += 1
        print("You Win!")
    else:
        print("Please enter a valid choice")
        break
print(f"Wins: {win}\nLoss: {loss}\nTies: {tie}")