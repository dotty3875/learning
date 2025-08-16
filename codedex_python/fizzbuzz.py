"""Create a fizz_buzz.py program that outputs numbers from 1 to 100.

Here's the catch:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz"."""

for i in range(1,101): # you can avoid the 0 in range by putting a 1 first
  if i % 3 == 0 and i % 5 == 0: # the module aka % is a divison in python, so this is saying if the number divided by 3 = 3, do this
    print(f'FizzBuzz') # the combined fizzbuzz needed above the fizz and buzz or else it would not print fizzbuzz, since the others were processed and printed first
  elif i % 3 == 0: 
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)