import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_iput = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_iput == "q":
        break
    
    if user_iput not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_iput == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_iput == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_iput == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_iput == computer_pick:
        print("You and the computer tied!")
        continue

    else:
        print("You lost!")
        computer_wins += 1

if user_wins != 1:
    print(f"You won {user_wins} times.")
else:
    print("You won 1 time.")

if computer_wins != 1:
    print(f"The computer won {computer_wins} times.")
else:
    print("The computer won 1 time.")

print("Goodbye!")