"""Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below."""

# Write your solution here
def squared(string, num):
    string = string * (num * num) # keeps the string large enough to work with regardless of num input 
    track = 0 
    start = 0
    while track != num:
        print(string[(start):(start + num)]) # keeps it starting on the right after the last place it stopped
        track += 1 
        start += num


# Testing the function
if __name__ == "__main__":
    squared("abc", 5)
