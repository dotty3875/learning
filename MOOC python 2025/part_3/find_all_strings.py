"""Please make an extended version of the previous program, which prints out all the substrings which are at least three 
characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long."""

#my second attempt with helpful explainations from chatgpt

string = input("Pleaes type in a word: ")
letter = input("Please type in a character: ")
index = string.find(letter)
while True:
    if index + 3 > len(string): 
        break
    else:
        print(string[index: index + 3])
        index = string.find(letter, index + 1)
    if index == -1:
        break

################################################################################################################################################################################
#5/6/2025
#this one above is functional

# the part i was not grasping was that theres two parts to a .find - string.find(word, slice indeces). by default the indeces is 0 and it follows a comma for the word in a find
# which tells the program "look from 0" and if you want it to not tread over ground you've already covered you need to tell it to you need to refer it back to what its already
# looked for in the term of the index + 1. the +1 makes sure it doesnt catch the same part of the index you've printed e.g. string = iee iei iea if you didnt have the +1 it would
# print "iee" then "iei" and it would see the ending i of the "iei" and print "iie" with the a of "iea" being a remaining and it would not print that last line. 

#tl;dr after comma you asign the start point of the search aka string.find(word, WHERE IT STARTS IN INTEGER), modify it to change output each loop

#################################################################################################################################################################################

# i could not wrap my head around this


word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = 0

while i < len(word)-2:
    if word[i] == char:
        print(word[i:i+3])
    i += 1


#reading it here makes sense but i couldnt put pen to paper when writing it myself


# i tried this sort of stuff to no avail

"""# Write your solution here
string = input("Pleaes type in a word: ")
letter = input("Please type in a character: ")
track = 0 

while track < len(string):
    index = string.find(letter, track)
    print(string[index:index + 3])
    track += 1


# Write your solution here
string = input("Pleaes type in a word: ")
letter = input("Please type in a character: ")
index = string.find(letter)


while index < len(string):
    index = string.find(letter, index)
    if len(string[index:index + 3]) <= 2:
        pass
    else:
        print(string[index:index + 3])
        index += 1"""



