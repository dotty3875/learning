name = input("What is your name? ")

print(f'Welcome to the adventurers path {name} youre in for a ride')


answer = input(
    "you are on a dirt path, you reach the end. left or right? ").lower()

if answer == "left":
        answer = input("you're at a river. you can walk around it or swim across. do you SWIM or go AROUND? ").lower()

        if answer == "swim":
            print("you swam across and were eaten by an alligator. you die")

        elif answer == "around":
            print("you walked for many miles, you ran out of water. you die")
        else:
            print("invalid option. you die")

elif answer == "right":
    answer == input("you're at a rickety bridge. do you cut the ropes or go across? ROPES or ACROSS? ").lower()
        
    if answer == "ropes":
            answer == input("you cut the ropes. the bridge falls and forms a ladder down to the pit. you go to the pit. it is pitch black. do you turn back or try to go through the dark? DARK or BACK? ").lower()

            if answer == "back":
                print("you tire yourself out climbing on the ladder and fall to your death. you die")
                
            elif answer == "dark":
                answer == input("you progress further into the darkness, what now?")

            else: 
                print("you die.")            

    elif answer == "across":
        print("it breaks as you go across. you die")
        
    else: 
        print("invalid, you die.")
    #make sure identation is valid and you keep track of which answers match wiht what or its a big mess
else:
    print("not valid, try again from the start")
    quit()