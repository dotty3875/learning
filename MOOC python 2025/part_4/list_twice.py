"""Please write a program which asks the user to type in values and adds them to a list. After each addition, the list is printed out in two different ways:

in the order the items were added
ordered from smallest to greatest
The program exits when the user types in 0."""

# Write your solution here

list = []
while True:
    newItem = int(input("New Item: ")) # int required or will be treated as string and will display incorrect when sorted, as well as breaking the line 12 if statement
    if newItem == 0: 
        break
    list.append(newItem)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}") # syntax for sorted is sorted(list) not list.sorted() as .sorted() does not return result - very different 

print("Bye!")