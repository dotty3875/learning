"""Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character,
 from the shortest to the longest. Have a look at the example below."""


input_string = input("Please type in a string: ")
letters = 0
loops = len(input_string)
while loops != 0:
    loops -= 1
    letters -= 1
    print(input_string[letters:])
