"""Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line."""

# Write your solution here
tries = 0
track = 0
string = input("Please type in a string: ")

while track != len(string): 
    tries -= 1
    track += 1
    print(string[tries])
    
# be sure that if you're trying to len(string) - tracking_variable, make sure that the tracking variable is being added each loop 
# or else it will be like doing 1 - - 1 in maths, which is a plus and it tries to skip too far ahead instead of doing -1 -2 -3 -4, it will go -1 2 5 or something 
# else that gives a string index error as those might not exist in that string



# new way 


string = input("PLease type in a string: ")
track = 0
while track < len(string): 
    track += 1
    print(string[len(string) - track])
