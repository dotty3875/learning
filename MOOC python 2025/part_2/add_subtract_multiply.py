# Write your solution here

number1 = int(input("What is your first number? "))
number2 = int(input("What is your second number? "))
operation = input("What operation? add, subtract, or multiply? ")

if operation == "multiply":
    total = number1 * number2
    print(f'{number1} * {number2} = {total}')
elif operation == "add":
    total = number1 + number2
    print(f'{number1} + {number2} = {total}')
elif operation == "subtract":
    total = number1 - number2
    print(f'{number1} - {number2} = {total}')
else:
    pass #code does nothing if invalid operation 