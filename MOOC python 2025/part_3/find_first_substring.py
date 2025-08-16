"""Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program."""


# Write your solution here
string = input("Pleaes type in a word: ")
letter = input("Please type in a character: ")

index = string.find(letter)

if len(string[index:index + 3]) <= 2:
    pass
else:
    print(string[index:index + 3])


#creator solution

word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = 0

while i < len(word)-2:
    if word[i] == char:
        print(word[i:i+3])
        break
    i += 1


#second try

string = input("Pleaes type in a word: ")
letter = input("Please type in a character: ")
index = string.find(letter)
if index + 3 > len(string): 
    print()
else:
    print(string[index: index + 3])