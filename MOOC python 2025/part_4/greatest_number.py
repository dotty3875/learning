"""Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three."""

# Write your solution here
def greatest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # must be >= or something like 1,1,-100 will return -100 falsely
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest) # can skip a step and just print(greatest_number(1, 1, -100)) but this is how it was prompted so i left it be