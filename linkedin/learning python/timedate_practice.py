from datetime import datetime, date, timedelta # comma to import several modules 

today = date.today() # today's full date
print("today's date", today)

print("Date components: ", today.day, today.month, today.year) # each individual component of the date

print("Today's weekday number", today.weekday(), end="") # 0 = mon, 6 = sun - days of the week as numbers, used as reference below
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
print(" which is a", days[today.weekday()]) 

today2 = datetime.now() # time and date down to the millisecond
print("current date and time is", today2) 

time = datetime.time(datetime.now()) # just time, no date. datetime.time() is the class and datetime.now() is the object
print("current time is", time)

##################################################################################################################################################################################################

now = datetime.now()
print(now.strftime("The current year is: %Y")) # formatted to only show current year
print(now.strftime("%a, %d %B, %y"))

print(now.strftime("Locale date and time: %c ")) # local time and date in local format (doesnt work right for Australia D/M/Y format)
print(now.strftime("Locale date: %x ")) # only local date
print(now.strftime("Locale time: %X ")) # only local time

print(now.strftime("Current time: %I:%M:%S %p")) # %I - 12 hour time, %H - 24h time, %M - minutes, %S seconds, %p - local AM/PM
print(now.strftime("Current time: %H:%M")) # 24h time, no seconds

###################################################################################################################################################################################################

# timedelta refers to a span of time, not a specific time/day

print(timedelta(days=365, hours=5, minutes=1)) # 365 days, 5:01:00 - creates span of time

print("Today is", now)
print("In one year, it will be:", now + timedelta(days=365)) # + 365 days to current date
print("In two weeks and three days it will be:", now + timedelta(days=3, weeks=2)) # + 3 days and 2 weeks to current day

weekAgo = datetime.now() - timedelta(weeks=1) # current date minus one week
print("One week ago it was", weekAgo.strftime("%A %B %d, %Y")) # week formatted

aprilFools = date(today.year, 4, 1)

if aprilFools < today: 
    print("April fools already went by", (today - aprilFools).days, "days ago")
    aprilFools = aprilFools.replace(year=today.year + 1) # updates aprilFools to look for next year's april fools

nextAF = aprilFools - today # next april fools is equal to next years april fools minus today's date
print("It's just", nextAF.days, "days until April Fools' Day") # .days specifies the time delta to output day amount instead of week, month, etc.