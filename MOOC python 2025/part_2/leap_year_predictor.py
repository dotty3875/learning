"""Please write a program which asks the user for a year, and prints out the next leap year.

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:"""



# Write your solution here
year = int(input("Year:"))
nextYear = year + 1

while True:
    if nextYear % 4 == 0 and nextYear % 100 != 0 or nextYear % 400 == 0:
        break
    nextYear += 1
print(f"The next leap year after {year} is {nextYear}")   


#code from creator, had issue with my similar one with 1904 
#lot simpler too