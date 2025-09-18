def count_numbers(which, numbers):
    # Your code goes here
    which = which.lower()
    evenTotal = 0
    oddTotal = 0
    if which == "even":
        for i in numbers:
            if i % 2 == 0:
                evenTotal += 1
        return evenTotal
    if which == "odd":
        for i in numbers:
            if i % 2 != 0:
                oddTotal += 1
        return oddTotal
    if which != "even" or which != "odd":
        return -1



numbers= [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
result = count_numbers("odd", numbers)
print(result)