"""Please write a program which asks the user to choose between addition and removal. Depending on the choice, 
the program adds an item to or removes an item from the end of a list. The item that is added must always be one greater than
 the last item in the list. The first item to be added must be 1."""

# Write your solution here
array = []
track = 1
choice = ""
while choice != "x":
    print("The list is now", array)
    choice = input("a(d)d, (r)emove or e(x)it: ").lower()

    if choice == "d":
        array.append(track)
        track += 1
    
    elif choice == "r":
        if array != []: # this if ensures that if the list is empty there wont be an error and will continue until "x"
            array.pop(track - 2) # -2 needed or will try to .pop an index that does not yet exist
            track -= 1 # keeps list linearly going i.e 1,2,3,4 - 1,2,3 - 1,2 - 1,2,3
        else: 
            continue # returns back to the choice input
print("Bye!")