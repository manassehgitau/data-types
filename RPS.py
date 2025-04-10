import random

rounds = 10
choices = ['rock', 'paper', 'scissors', 'quit']

name = input("Enter your name: ").title()
answer = ""

computer_marks = 0
user_marks = 0

while rounds > 0 and answer != "quit":
    answer = input("Rock 🪨, paper 📃 or scissors ✂️: ").lower()
    computer_choice = random.randint(0, 2)

    print(f"\ncomputer: {choices[computer_choice]}")

    if choices[computer_choice] == "scissors" and answer == "paper":
        computer_marks += 1
        print("You lose 😓. computer wins 🖥️\n")
    elif choices[computer_choice] == "paper" and answer == "scissors":
        user_marks += 1
        print("You win 😉\n")
    elif choices[computer_choice] == "paper" and answer == "rock":
        computer_marks += 1
        print("You lose 😓. computer wins 🖥️\n")
    elif choices[computer_choice] == "rock" and answer == "paper":
        user_marks += 1
        print("You win 😉\n")
    elif choices[computer_choice] == "rock" and answer == "scissors":
        computer_marks += 1
        print("You lose 😓. computer wins 🖥️\n")
    elif choices[computer_choice] == "scissors" and answer == "rock":
        user_marks += 1
        print("You win 😉\n")
    elif choices[computer_choice] == answer:
        print("Its a Draw 😁. No marks awarded\n")
    else: 
        print("I don't recognize your answer. Try again\n")
    rounds -= 1


print(f"Total Scores:\n computer 🖥️: {computer_marks} \n {name} 🥸: {user_marks} \n")

if user_marks > computer_marks:
    print(f"{name} wins 🏆.")
elif computer_choice < user_marks:
    print("You lose 😓")
else: 
    print("Its a Draw 😁")

# retry = input("Do you want to try again (yes/no): ").lower()

# if retry == "yes":
#     rounds = 10
