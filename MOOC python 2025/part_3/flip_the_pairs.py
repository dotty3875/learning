"""Please write a program which asks the user to type in a number. The program then prints out all the positive integer
 values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. 
 That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details."""





# Write your solution here

num = int(input("Please type in a number: "))
track = 1
pair1 = 1 #not sure if i can rephrase to use and print track instead of this helper but couldnt figure it out and dont care enough to dedicate more time to it
while num != 0 and num > 0: #prevents negative numbers or 0 from creating an infinite loop - can skip this line altoether with minor tweaks 
    while track != num and track <= num: 
        track += 2
        print(pair1 + 1)
        print(pair1)
        pair1 += 2
    if num % 2 != 0: #exists because if it lands on an even it will print an extra line exceeding num eg num = 4 this line will print "5". this modulo is protection against that
        print(pair1)
    break


#creator solution - which is doing what i said about removing the helper variable being possible

number = int(input("Please type in a number: "))

i = 1 #the tracking number is also the helper variable being printed 

while i <= number:
    if i+1 <= number: #prevents the extra print on uneven numbers
        print(i+1)
    print(i)
    i += 2