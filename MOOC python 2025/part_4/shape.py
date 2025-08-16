"""Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it.
 The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character 
 of the rectangle. The function prints first the triangle, and then the rectangle below it."""

# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    if word == "":
        word = "*"
    print(num * word[0:1])

def shape(sizeTriangle, strTriangle, sizeSquare, strSquare):
    # You should call function line here with proper parameters
    track = 0
    while track <= sizeTriangle:
        line(track, strTriangle)
        track += 1
    track = 0 # reset for next track helper variable 
    while sizeSquare != track:
        line(sizeTriangle, strSquare) # sizeTriangle instead of sizeSquare because it's meant to be in line with the triangle according to the tester
        track += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o") # sizeSquare is redundant but this current version is what the scope of the question is after