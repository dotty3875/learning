"""Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase."""






letter1 = str(input("1st letter: ")).upper()
letter2 = str(input("2nd letter: ")).upper()
letter3 = str(input("3rd letter: ")).upper()

if letter1 > letter2 > letter3 or letter1 < letter2 < letter3:
    print(f'The letter in the middle is {letter2}')
elif letter2 > letter1 > letter3 or letter2 < letter1 < letter3:
    print(f'The letter in the middle is {letter1}')
else:
    print(f'The letter in the middle is {letter3}')
