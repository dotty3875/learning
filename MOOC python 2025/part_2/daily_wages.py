# Write your solution here
day_multiplier = 0 
wage = float(input("What is your hourly wage? "))
hours = float(input("How hours did you work? "))
day = input("What day of the week did you work? ").lower()


#for some reason, if == "sunday" or "Sunday" it always becomes 2 and be changed, in this case lower
#but you can also change it to be if day == "Sunday" or day=="sunday"
if day == "sunday":
    day_multiplier = 2 
elif day != "sunday":
    day_multiplier = 1

total = (wage * hours) * day_multiplier

print(f'Daily wages: {total} euros')