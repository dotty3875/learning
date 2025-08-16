# Write your solution here

number =  float(input("Please type in a number with decimal points: "))
print(f'integer part: {int(number)}')
print(f'float part: {float(number) - int(number)}')

#this will seperate just the integer part, which always rounds down to the nearest whole number
#the second part seperates JUST the decimal point of the float