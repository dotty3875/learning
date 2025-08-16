"""Please write a function named chessboard, which prints out a chessboard made 
out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:"""


# Write your solution here
def chessboard(num):
    string = "10" * num # linear growth of string to match input num
    track = 0 
    while track != num:
        print(string[(0 + track):(num + track)]) #this splicing keeps it moving ahead by 1 step meaning it goes from 101 to 010 along the rest of the "string" variable
        track += 1 #keeps the track in check with the number inputed


# Testing the function
if __name__ == "__main__":
    chessboard(3)