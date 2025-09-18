"""The Python string method isupper() returns True if a string consists of only uppercase characters.

Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument.
 The function returns a new list, containing only those items from the original which do not consist of 
 solely uppercase characters."""

def no_shouting(list):
    newList = []
    for i in list:
        if i.isupper() == False: # if current i is not fully uppercase:
           newList.append(i) # add to non-uppercase list
    return newList

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)