"""Please write a function named length_of_longest, which takes a list of strings as its argument. The function
 returns the length of the longest string."""

def length_of_longest(list):
    temp = "" # helper to be used as comparison point for the reigning champion of largest string
    for i in list:
        if len(i) > len(temp):
            temp = i # assigns new largest string as temp
    temp = len(temp) # converts the longest string to int
    return temp

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)
