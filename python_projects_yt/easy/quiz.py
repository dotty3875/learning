score = 0

print(f'welcome to my computer quiz')

playing = input(f'do you want to play my game? Y or N ').upper()

if playing != "Y":
    quit()

print("Alright, lets play!")

answer = input("What does cpu stand for? ").lower() #make sure its .lower() not just .lower or else it breaks


if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Nope!")

answer = input("What does gpu stand for? ").lower()


if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Nope!")

answer = input("What does psu stand for? ").lower()


if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Nope!")

answer = input("What does ram stand for? ").lower()


if answer == "random access memory":
    print("Correct! Thanks for playing.")
    score += 1
else:
    print("Nope!")



print(f'you got {score} questions correct! nice')
print(f'which is {score / 4 * 100}% corrections correct')