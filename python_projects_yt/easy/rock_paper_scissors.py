import random

user_wins = 0 
computer_wins = 0 

options = ["rock", "paper", "scissors"] #list, type or data structure 


while True: 
    user_input = input("Rock, paper, or scissors? or type Q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]: #list of user inputs
        continue   
    random_number = random.randint(0, 2) #0 = rock, 1 = paper, 2 = scissors
    computer_pick = options[random_number]
    print(f'computer picked {computer_pick}.')

    if user_input == "rock" and computer_pick == "scissors":
        print(f'you won!')
        user_wins += 1 

    elif user_input == "paper" and computer_pick == "rock":
        print(f'you won!')
        user_wins += 1 

    elif user_input == "scissors" and computer_pick == "paper":
        print(f'you won!')
        user_wins += 1
    
    elif user_input == computer_pick:
        print("You and the computer tied!")
        continue
    
    else:
        print(f'you lost!')
        computer_wins += 1



print(f'you won {user_wins} times, and the computer won {computer_wins}.')
print("goodbye!")
