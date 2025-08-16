word = input("Please type a word: ")


if len(word) == 1 or len(word) == 0: 
    print("Thank you!")
else:
    print(f'There are {len(word)} in the word {word}\nThank you!')
#the len function will count amount of letters in a string
#you can embed functions in an fstring by doing so, spiky brackets around the main thing and circle brackets 