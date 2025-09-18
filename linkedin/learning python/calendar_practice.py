import calendar

c = calendar.TextCalendar(calendar.SUNDAY) # .SUNDAY or .MONDAY sets the calender to start with that day (e.g. Su Mo Tu We Th Fr Sa)
str = c.formatmonth(2026, 1, 0, 0) # outline what year, month, etc you want
print(str)

hc = calendar.HTMLCalendar(calendar.SUNDAY) # HTML for a calendar
str2 = hc.formatmonth(2026, 1)
print(str2)

for i in c.itermonthdays(2026, 8): # iterates through specified month (august 2026) and prints out all days. lots of 0 in output to show start/end of weeks for that month belong to another month
    print(i)

for name in calendar.month_name: # prints out name of each month. based on where locale of system
    print(name)

for day in calendar.day_name: # prints out each day of the week. based on locale of system
    print(day)

print("Team meetings will be on: ")
for m in range(1, 13): # starts on 1, ends at 12. 2nd variable for range is always -1 
    cal = calendar.monthcalendar(2026, m) # iterates through each month
    print("this is cal", cal)
    weekOne = cal[0] 
    weekTwo = cal[1]
    if weekOne[calendar.FRIDAY] != 0: # checks if the first week has 0, if so it's part of the previous months week and needs to go to the else
        meetDay = weekOne[calendar.FRIDAY]
    else: 
        meetDay = weekTwo[calendar.FRIDAY] # the second week's friday which is 100% part of august is the meetDay
    print(f"{calendar.month_name[m]}: {meetDay}")