#PART 1-4
# Write your solution here

students = int(input("How many students on the course? "))
desired_size = int(input("Desired group size? "))

groups = students // desired_size #needs modulo to solve
if students % desired_size != 0:  #if theres is a NOT a remainder of 0 
    groups += 1  #add 1 to group size to prevent undersized groups due to whole groups only

print(f'Number of groups formed: {groups}')