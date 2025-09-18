"""Please write a function named sum_of_positives, which takes a list of integers as its argument. The function 
returns the sum of the positive values in the list."""

def sum_of_positives(list):
    positiveList = []
    for i in list:
        if i > 0:
            positiveList.append(i) # adds all positive integers to list
    result = sum(positiveList) # adds all integers together to return sum
    return result

if __name__ == "__main__":
    list = [1,2,3,4,5,6]
    print("The result is", sum_of_positives(list))