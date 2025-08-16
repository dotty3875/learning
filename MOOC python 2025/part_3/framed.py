"""Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations."""


# Write your solution here

string = input("Please type in a string: ")

spaceFormat1 = "*"
spaceFormat2 = " "

def middle():
    middle = spaceFormat1 + string + spaceFormat2
    return middle # just made this function to not repeat the same middle = space over and over and over 

middle()
while len(middle()) < 28:
    spaceFormat1 += " "
    spaceFormat2 += " "
    middle()

if len(middle()) <= 28:
    spaceFormat1 += " "
spaceFormat2 += "*"
print("******************************")
print(middle())
print("******************************")


#creator solution

# Write your solution here
word = input("Word: ")

start = (28 - len(word)) // 2
if len(word) % 2 == 0: 
    end = start
else:
    end = start+1 #if its odd then it adds 1 to make sure it fits nicely, which i did instead by doing len <= 28 before adding or not adding a space at start 


print('*' * 30)
print(f"*{(start * ' ')}{word}{(end * ' ')}*")
# print(f"*{word.center(28)}*")
print('*' * 30)


#second try 

string = input("Word: ")

leftmid = "*" + (" " * ( 14 - len(string))) 
rightmid = (" " * ( 14 - len(string)))
middle = leftmid + string + rightmid
flip = 0
while len(middle) < 28:
    middle = leftmid + string + rightmid
    if flip % 2 == 0: #to flip between adding to  left and right
        leftmid += " "
    else:
        rightmid += " "
    flip += 1


rightmid += "*" #didnt have it earlier
middle = leftmid + string + rightmid #need to re-state this so that the len right below can read correctly with the asteriks or it will always be 28 
if len(middle) == 29:
    leftmid += " "
print("******************************")
print(f"{leftmid}{string}{rightmid}")
print("******************************")
