"""Please write a program which asks the user for a positive integer N. The program then prints out all numbers between
 -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line."""

# Write your solution here
num = int(input("Please type in a positive integer: "))

for i in range(-num, num + 1): # + 1 required to make sure it ends on the proper number not 1 short e.g. 4 when input is 5 
    if i != 0: # prevents 0 being printed
        print(i)