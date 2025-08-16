###################################################################################
#the tutorial for this, again, is not functional properly
#a user on github added features and corrected issues, and is the commented out section below the end of this
#####################################################################################




import random

def roll(): #def goes towards the top kind of like import
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


tutorial = input("Do you know how to play PIG? y or n ")

if tutorial != "y":
    print("The goal of the game of pig is to get to 50, you will have turns to take in order to reach it. if you hit a 1 your score is reset to 0. after reaching 50 you can keep going to get a higher score, but past 50 the other players are automatically eliminated if they cannot reach 50. person with the highest score wins")
elif tutorial == "y":
    pass
else: 
    print("error")


while True:
    players = input("Enter the number of players: 2-4 ")
    if players.isdigit(): #checks if valid integers are here
        players = int(players) #
        if 2 <= players <= 4:
            break
        else:
            print("must be valid number of players")
    else:
        print("invalid try again")
        
max_score = 50 
player_scores = [0 for _ in range(players)] #list comprehension - adds 0 per each player of list 

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer number", player_idx + 1, "turn has just started! ")
        print("your total score is", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1. Turn done!") 
                current_score = 0 
                break
            else: 
                current_score += value
                print("you rolled a: ", value) #always add comma to diferenciate from string

            print("Your score is:", current_score)    

        player_scores[player_idx] += current_score
        print("Your total score is", player_scores[player_idx])
        

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of", max_score) #not sure why this is not working
quit()


'''import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


def print_scores(players_scores):
    print("\nCurrent Scores:")
    for idx, score in enumerate(players_scores):
        print(f"Player {idx + 1}: {score}")
    print("-" * 20)

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

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

         # Update player's total score
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {player_scores[player_idx]}")

   # Check if the player has won
        if player_scores[player_idx] >= max_score:
            print(f"\n🎉🎉 Player {player_idx + 1} has won with a total score of {player_scores[player_idx]}! 🎉🎉")
            break

    print_scores(player_scores)

    # Continue the game if no winner
    if max(player_scores) < max_score:
        print("\nNext round starting!")
        continue
    else:
        # Break the outer loop if a player has won
        break'''