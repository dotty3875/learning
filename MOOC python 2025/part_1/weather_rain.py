# this is overkill of the def() function but good practice
#there is a much simpler way of doing this but this way is modular 



def jeans():
    print("Wear jeans and a t-shirt")

def umbrella():
    print("Dont forget your umbrella!")

def jumper(): 
    print("I reccomend a jumper as well!")

def jacket():
    print("Take a jacket with you")
        
def umbrella():
   print("Don't forget your umbrella!")

def cold(): 
    print("Make it a warm coat, actually \nI think gloves are in order")
      


temperature = int(input("What is the weather forecast for tomorrow? \nWhat is the temperature? "))
rain = input("Will it rain? y or n ").lower()

if temperature >= 20 and rain == "n":
    jeans()
    

elif temperature >= 20 and rain != "n":
   jeans()
   umbrella()
    
elif temperature >= 10 and rain == "n":
    jeans()
    jumper()
    jacket()

elif temperature >= 10 and rain != "n":
    jeans()
    jumper()
    jacket()
    umbrella()

elif temperature >= 5 and rain == "n":
    jeans()
    jumper()
    jacket()
    cold()
    
elif temperature >= 5 and rain != "n":
    jeans()
    jumper()
    jacket()
    cold()
    umbrella()