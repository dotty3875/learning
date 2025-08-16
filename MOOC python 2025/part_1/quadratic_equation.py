"""We will return to the concept of a module and the import statement later. For now, it is sufficient to understand that the line from math import sqrt 
allows us to use the sqrt function in our program.

Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the 
quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above formula will always work."""


from math import sqrt

a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))

# formula: x = (-b ± sqrt(b²-4ac))/(2a).

discriminant = b**2 - (4 * a * c)

sol1 = (- b - sqrt(discriminant)) / (2 * a) 
sol2 = (- b + sqrt(discriminant)) / (2 * a)

print(f'The roots are {sol1} and {sol2}')