import calendar

def count_days(year, month, whichday):
    total = 0
    # c = calendar.TextCalendar(calendar.MONDAY) # for testing 
    # print(c.formatmonth(year, month)) # for testing
    for i in calendar.monthcalendar(year, month): # contains list of each week present for that month including the end and start as 0 if its from another month
        if i[whichday] != 0:
            total += 1 # keeps track of the amount of "whichday" present in that month
    
    return total


testyear = 2025
testmonth = 7
testday = 0
result = count_days(testyear, testmonth, testday)
print(result)