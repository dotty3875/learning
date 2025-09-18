"""Please write a function named all_the_longest, which takes a list of strings as its argument. The function should return a new
 list containing the longest string in the original list. If more than one are equally long, the function should return all of the 
 longest strings."""

def all_the_longest(list):
    longest = []
    helper = ""
    for i in list:
        if len(i) >= len(helper):
            helper = i # this first instance finds the longest in the list
    for i in list:
        if len(i) == len(helper): # this loop compares the entire list to the length of the longest one found above
            longest.append(i) 
    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]            
    result = all_the_longest(my_list)
    print(result)