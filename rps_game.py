from object import rock, paper, scissors
from random import choice 
from os import system, name

print()
print("**********Welcome to Rock, Paper, Scissors Game!**********")
print()

playing = input("Do you want to play the game? [yes/no] ").lower()

if playing != "yes":
    quit()

def check_win(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "draw"
    elif computer_choice == rock and user_choice == paper:
        return "user"
    elif computer_choice == paper and user_choice == scissors:
        return "user"
    elif computer_choice == scissors and user_choice == rock:
        return "user"
    else:
        return "computer"

list_of_objects = [rock, paper, scissors]
computer_score = 0
user_score = 0

play = True
while play:
    computer_choice = choice(list_of_objects) # selects a random object.
    user_choice = input("Choose: rock(r), paper(p) or scissors(s): ").lower()
    if (user_choice not in ["rock", "paper", "scissors"]) or (user_choice not in ['r', 'p', 's']):
        print("Please, ",end="")
        continue

    if user_choice == "rock" or user_choice == 'r':
        user_choice = list_of_objects[0]
    elif user_choice == "paper" or user_choice == 'p':
        user_choice = list_of_objects[1]
    else:
        user_choice = list_of_objects[2]

    win = check_win(computer_choice, user_choice)
    print()
    print("*"*40)
    print(f"You choose: {user_choice}\nComputer choose: {computer_choice}")

    if win == "user":
        user_score += 1
        print("You won!")
    elif win == "computer":
        computer_score += 1
        print("You lost!")
    else:
        print("Draw!")
    print()
    print("*"*40)
    print(f"Scoreboard:\nYou: {user_score}\nComputer: {computer_score}")
    print("*"*40)
    play = input("Do you want to play again? [yes/no] ").lower()
    if play != "yes":
        play = False
        print("Thanks for playing the game, Bye :) ")
    else:
        system('cls' if name == 'nt' else 'clear')
        play = True