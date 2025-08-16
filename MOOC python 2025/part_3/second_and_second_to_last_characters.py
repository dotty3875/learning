"""Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to 
last character are the same or not. See the examples below."""



# Write your solution here
string = input("Please type a string: ")


#ord() function calls forth the assigned ASCII ordinal number of a string
#in this case i am using it to convert a single letter into a number and then compare those two numbers and if they're the same then it can work properly
if (ord(string[1]) % ord(string[-2]) == 0): 
    print(f"The second and the second to last characters are {string[1]}")
else: 
    print("The second and the second to last characters are different")



#the provided answer is a lot clearer and does not use ord 

word = input("Please type in a string: ")
second = word[1]
secondLast = word[-2]
#when counting from the start, 0 is the first letter
#when counting from the back, -1 is the last letter
#[1] is 2nd letter from left, [-2] is second letter from right


if second != secondLast:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {second}")

#it's just assigning those values to be second and second last then comparing the two letters, rather than converting them to numbers to compare with modulo