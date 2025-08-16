"""Pre-task
Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

Part 1: Count
After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

You will need a new variable here to keep track of the numbers typed in.

Part 2: Sum
The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

The program should now print out the following:

Part 3: Mean
The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.


Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation."""

# Write your solution here
num_list = int()
num_track = int()
num_mean = int()
num_positive = int()
num_negative = int()

print("Please type in integer numbers. Type in 0 to finish. ")
while True: 
    num = (str(input("")))

    if int(num) > 0:
        num_positive += 1
    elif int(num) < 0: 
        num_negative += 1

    num_track += 1

    if num == "0":
        num_track -= 1
        break
        
    num_list += int(num) 
    num_mean = int(num_list) / int(num_track)

print(f"Numbers typed in {num_track}")
print(f"The sum of the numbers is {num_list}")
print(f"The mean of the numbers is {num_mean}")
print(f"Positive numbers {num_positive}")
print(f"Negative numbers {num_negative}")