"""Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument."""

# Copy here code of line function from previous exercise
def line(num, word):
    if word == "":
        word = "*"
    print(num * word[0:1])

def triangle(size):
    # You should call function line here with proper parameters
    track = 1 
    while track <= size:    
        line(track, "#")
        track += 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
