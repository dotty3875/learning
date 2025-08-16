"""Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

"""

input_string = input("Please type in a string: ")
letters = 0
loops = len(input_string)
while loops != 0:
    print(input_string[:letters])
    loops -= 1
    letters += 1
print(input_string[:letters])


#creator solution

word = input("Please type in a string: ")
i = 0
sum = ""
while i < len(word):
    sum += word[i]
    print(sum)
    i += 1


#second try

string = input("Please type in a string: ")
flux = 1
for i in range(len(string)):
    print(string[0:flux])
    flux += 1