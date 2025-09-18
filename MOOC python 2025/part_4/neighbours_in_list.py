"""Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4."""

def longest_series_of_neighbours(list):
    memory = list[0] # starts the memory at the first index, used as comparison between current i and previous num
    neighbour = 0 
    largest = 0
    for i in list:
        if i + 1 == memory or i - 1 == memory: # checks if i is a neighbour to previous number (stored as memory variable)
            neighbour += 1
        if neighbour >= largest: # keeps track of the largest neighbour streak as the for loop iterates through the list
            largest = neighbour
        if i + 1 != memory and i - 1 != memory: # "and" required instead of "or" so it doesn't always pass. this checks if the current neighbour streak broke and resets if yes
            neighbour = 0 
        memory = i
    largest += 1 
    return largest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))