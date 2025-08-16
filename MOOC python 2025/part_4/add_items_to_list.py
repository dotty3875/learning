"""Please write a program which first asks the user for the number of items to be added. 
Then the program should ask for the given number of values, one by one, and add them to a 
list in the order they were typed in. Finally, the list is printed out."""

# Write your solution here
array = []
changes = int(input("How many items: "))
track = 1
while track <= changes:
    array.append(int(input(f'Item {track}: ')))
    track += 1
print(array)
