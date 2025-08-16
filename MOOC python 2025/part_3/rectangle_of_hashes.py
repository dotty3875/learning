"""Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly"""


# Write your solution here

width = int(input("Width: "))
height = int(input("Height:"))
tall = 0
while height != tall:
    print(width * "#")
    height -= 1




#creator solution


# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))

i = 1

while i <= height:
    print("#" * width)
    i += 1