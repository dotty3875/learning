"""Please write a function named formatted, which takes a list of floating point numbers as its argument. The function returns a new 
list, which contains each element of the original list in string format, rounded to two decimal points. The order of the items in the
 list should remain unchanged.

Hint: use f-strings to format the floating point numbers into suitable strings."""

def formatted(list):
    formattedList = []
    for i in list:
        formattedList.append(f"{i:.2f}") # {i:.2f} takes current i from the list, and gives it only two decimals after the dot, f meaning float 
    return formattedList

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)