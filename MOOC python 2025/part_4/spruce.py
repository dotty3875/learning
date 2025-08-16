"""Please write a function named spruce, which takes one argument. 
The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument."""

# Write your solution here
def spruce(num):
    print("a spruce!")
    stem = num
    middle = "*"
    while num != 0:
        print((" " * (num - 1)) + middle) # the -1 brings it closer to the left side of the terminal (as per the testing criteria)
        middle += "**"
        num -= 1
    print((" " * (stem - 1)) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(10)