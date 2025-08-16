"""Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:"""


# Write your solution here

num = int(input("Please type in a number: "))
multiply1 = 1 
multiply2 = 1
while multiply1 <= num:
    while multiply2 != num:
        print(f"{multiply1} x {multiply2} = {multiply1 * multiply2}")
        multiply2 += 1
    print(f"{multiply1} x {multiply2} = {multiply1 * multiply2}")
    multiply1 += 1 
    multiply2 = 1 


#creator solution

number = int(input("Please type in a number: "))
i = 1
while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1