import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 30
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1}, turn has just started!")
        print(f"Your total score is: {player_scores[player_idx]}. The player having the highest score at the end of the turn, while having at least {max_score} points, wins! Rolling a 1 removes all of your points.\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? Type 'y' to roll the dice or 'n' to end your turn: ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your score is: {current_score}")

        player_scores[player_idx] += current_score
        print(f"Your total score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx + 1}, is the winner with a score of: {max_score}")
            
