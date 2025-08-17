"""Please write a program which asks the user for words. If the user types in a word for the second time, the program should 
print out the number of different words typed in, and exit."""

# Write your solution here

track = 0
checker = 0 
array = []
unique = True
while unique == True:
    array.append(input("Word: "))
    while checker != track: # checks each indexed word against each other
        if array[checker] == array[track]:
            unique = False # breaks out of the outer loop
            break # breaks out of current checker loop
        else:
            checker += 1
    checker = 0 # resets the counter to the start to check for duplicate words
    track += 1
print("You typed in", track - 1, "different words") # -1 needed or will also include the duplicate word as a unique word

############## CREATOR SOLUTION ############
# far simpler 

# Write your solution here
list = []
while True:
    word = input("Word: ") # intermediary variable instead of directly appending so it can be checked 
    if word in list:  # simple iteration in a single loop instead of using 2 helper variables 
        print(f"You typed in {len(list)} different words")
        break
    list.append(word) # appends at end to prevent the "track - 1" duplicate word being counted as unique (line 20)
    
