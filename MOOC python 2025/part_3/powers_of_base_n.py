"""Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2)."""



# Write your solution here

limit = int(input("Upper limit: "))
base = int(input("Base: "))
num = 1

while num <= limit:
    print(num)
    num = num * base
