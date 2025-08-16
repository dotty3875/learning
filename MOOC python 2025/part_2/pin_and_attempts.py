"""Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. 
The program should then print out the number of times the user tried different codes.
If the user gets it right on the first try, the program should print out something a bit different:"""



# Write your solution here
pin = 4321
attempts = 0
while True:
    
    guess = int(input("What is the PIN code? ")) 
    attempts += 1
    if guess == pin and attempts == 1:
        print('Correct! It only took you one single attempt!')
        break
    elif guess == pin:
        print(f'Correct! It took you {attempts} attempts.')
        break
    else: 
        print("Wrong")
        #if attempts >= 3:
            #print("Too many wrong attempts.")
            #quit()
