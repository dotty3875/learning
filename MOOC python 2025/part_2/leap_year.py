"""Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not."""



year = int(input("Please type in a year: "))

if year % 4 == 0:
    if year % 400 == 0 and year % 100 == 0: 
        print("That year is a leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print("That year is a leap year")
    else:
        print("That year is not a leap year")
elif year % 4 != 0: 
    print("That year is not a leap year")


#ChatGPT simplified

year = int(input("Please type in a year: "))

#uses and/or instead of nested conditionals 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That year is a leap year")
else:
    print("That year is not a leap year")