"""Please write a program which asks the user to type in a number. 
The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below."""



# Write your solution here

num = int(input("Please type in a number: "))

track = 1
topNum = num

while track <= num / 2:
    print(track)
    print(topNum)
    topNum -= 1
    track += 1
if num % 2 != 0: #on odd numbers it wouldnt print the last thing so this is just checking if its odd then printing an extra one so its not missing
    print(track)



#creator solution


number = int(input("Please type in a number: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left)