import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print(f'please type a number larger than 0 next time')
        quit()
else: 
    print(f'please type a number next time')
    quit()

random_number = random.randint(0, top_of_range) #.randrange -1 to 11 will include numbers 0 to 10 - will not icnlude -1 and 11. .randint will include the upper and lower limits so it will have 11 and -1
guesses = 0 


while True: 
    guesses += 1 #will add +1 to guesses each and every loop
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Please type a number next time')
    
    if user_guess == random_number:
        print("you got it right!")
        break #if this is not here, even if correct it will ask for more guesses and wont progress
    elif user_guess > random_number:
            print(f'you were above the number')
    else: 
            print("you were below the number")

print(f'you got it in {guesses} guesses!')

