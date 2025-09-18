"""Please write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list."""

def even_numbers(list):
    evenList = []
    for i in list:
        if i % 2 != 0: # not equal to modulo 2 means any non-even numbers
            continue # skips odd numbers
        else:
            evenList.append(i)
    print("original", list)
    print("new ", end='')
    return evenList

if __name__ == "__main__":
    list = [1,2,3,4,5,6]
    print(even_numbers(list))