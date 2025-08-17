"""Please write a program which asks the user to type in a string. The program then prints each input character on a separate line. 
After each character there should be a star (*) printed on its own line."""

# Write your solution here
string = input("Please type a string: ")
for letter in string: # for being a type of definite iteration # you can assign any variable name for the "letter". must use .split() for words of a sentence (splits into list)
    print(letter)
    print("*")