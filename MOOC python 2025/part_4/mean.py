"""Please write a function named length which takes a list as its argument and returns the length of the list."""

# Write your solution here

def mean(list):
    mean = sum(list) / len(list) # sum() adds listed numbers together, divided by (/ for float) amount of numbers for mean
    return mean

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)