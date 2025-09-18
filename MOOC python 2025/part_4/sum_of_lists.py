"""Please write a function named list_sum which takes two lists of integers as arguments. The function returns a new list which contains 
the sums of the items at each index in the two original lists. You may assume both lists have the same number of items."""

def list_sum(a, b):
    newList = []
    helper = 0 
    for i in a:
        newList.append(a[helper] + b[helper]) # uses helper to keep track of what to append 
        helper += 1 
    return newList

if __name__ == "__main__":
    list1 = [1,2,3]
    list2 = [4,5,6]

    print(list_sum(list1, list2))