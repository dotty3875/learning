"""Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:"""


# chat gpt assisted with second_index. i was trying to feed index to index but this is simpler

string = input("Please type in a word: ")
letter = input("Please type in a substring: ")

first_index = string.find(letter)
second_index = string.find(letter, first_index + len(letter)) #need second index so it skips the first mention of the substring

if second_index != -1: # -1 is the default for the .find command if it cant find anything further in the string, basically saying 
                       # "it doesnt exist past the point you're trying to reach"
    print(f"The second occurrence of the substring is at index {second_index}.")
else:
    print("The substring does not occur twice in the string.")


#creator solution 

# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index1 = string.find(substring) #finds the first mention of the substring
index2 = -1 
if index1 != -1: #basically if there is no first mention of the substring
    index2 = string.find(substring, index1 + len(substring))  #this is saying if there is a first substring that is valid, make that the starting point for the search of 
    # the next substring. if the next substring is not valid it will default to -1 and end the program, but if its anything else that means it has found the second occurance

if index2 == -1: #if the above "if" did not run, that means there was no second string and it defaults to this "if"
    print('The substring does not occur twice in the string.')
else:
    print(f"The second occurrence of the substring is at index {index2}.")
