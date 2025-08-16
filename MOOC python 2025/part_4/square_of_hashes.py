"""Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, 
which determines the length of the side of the square.

The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise 
above the code for this exercise. Please don't change anything in the line function."""

# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        word = "*"
    print(num * word[0:1])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    track = 0 
    while track != size:
        line(size, "#")
        track += 1 # helper variable 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(10)
