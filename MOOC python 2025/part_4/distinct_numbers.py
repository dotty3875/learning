"""Please write a function named distinct_numbers, which takes a list of integers as its argument. The function returns a new list containing 
the numbers from the original list in order of magnitude, and so that each distinct number is present only once."""

def distinct_numbers(list):
    newList = []
    unique = 0
    list = sorted(list) # sorted so all 1's for example are beside each other 
    for i in list:
        if i != unique:
            newList.append(int(i))
        else:
            continue
        unique = int(i) # compares to last number, since sorted will allow for only unique numbers to be appended  
    return newList

if __name__ == "__main__":
    list = [3, 2, 2, 1, 3, 3, 1,4,5,1,2,3,4,1,5,1,2,3,4,5,1]         
    print(distinct_numbers(list))