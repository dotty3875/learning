"""Please write a function named shortest, which takes a list of strings as its argument. The function returns whichever of the strings
 is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation 
 in the tests). You may assume there will be no empty strings in the list."""

def shortest(list):
    temp = list[0] # helper variable for comparison 
    for i in list:
        if len(i) < len(temp): # as for iterates, searches for the smallest string present 
            temp = i
    return temp

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)