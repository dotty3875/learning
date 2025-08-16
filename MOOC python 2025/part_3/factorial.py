"""Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. 
Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of 
all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120."""


#my solution after an hour!

# wasted my time thinking it was meant to be, say input is 5, 5 x 1 + 5 x 2 so on so forth which was 75 but its really 1 x 2 x 3 x 4 x 5 = 120
# didnt know what a factorial really was!

# now that i look at it i can easily remove 2-3 lines that are redundant 
track = 0
maths = 1
while True:
    num = int(input("Pick a number: "))
    if num <= 0 or num <= -1: #super extra, can just be num <= 0: and be working just as well
        print("Thanks and bye!")
        break
    if track > num: #actually does nothing
        break  
    while track != num:
        track += 1
        maths *= track #messed around here too much trying to add them together then multiply instead of just multiply 
    track = 0
    print(f"The factorial of the number {num} is {maths}")
    maths = 1 #resets the loop so its not adding seperate factorials together 


# chat gpt solution 

while True:
    num = int(input("Enter a non-negative integer (negative to quit): "))
    if num < 0:
        print("Thanks and bye!")
        break

    result = 1                # reset for this number only
    for i in range(2, num + 1):
        result *= i           # multiply, don’t add

    print(f"The factorial of {num} is {result}")


# creator solution

factorial = 1
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial of the number {number} is {factorial}")
    factorial = 1
print("Thanks and bye!")
