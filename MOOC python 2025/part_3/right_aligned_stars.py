"""Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long."""

# Write your solution here

string = input("Please type in a string: ")
tries = 0
newString = ""

while len(newString + string) < 20:
    tries += 1
    newString = tries * "*"
    len(newString + string)

print(newString + string)



#creator answer

# Write your solution here
word = input("Please type in a string: ")
size = 20 - len(word)
print(("*" * size) + word)