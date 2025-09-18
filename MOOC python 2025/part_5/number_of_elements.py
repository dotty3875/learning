"""Please write a function named count_matching_elements(my_matrix: list, element: int), which takes a two-dimensional array of integers and a single integer
 value as its arguments. The function then counts how many elements within the matrix match the argument value."""

# Write your solution here
def count_matching_elements(my_matrix: list, element: int): 
    tracker = 0 # keeps track of matching elements
    for row in range(len(my_matrix)): # range looks for how many different rows there are in this matrix, loops through each row
        for index in my_matrix[row]: # for current row, look at each number at every available index
            if index == element: # compare current indexed number to the element number being searched for 
                tracker += 1

    return tracker

if __name__ == "__main__":
    m = [[3, 1, 5, 5, 4, 4], [1, 4, 3, 4, 2, 5], [5, 5, 4, 2, 1, 3]]
    print(count_matching_elements(m, 5))