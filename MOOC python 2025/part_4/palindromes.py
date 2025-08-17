"""Please write a function named palindromes, which takes a string argument and returns True if the 
string is a palindrome. Palindromes are words which are spelled exactly the same backwards and forwards."""

# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string):
    if string == string[::-1]: # [::-1] reads the string from end to start - reversing it
        return True # is palindrome
    else:
        return False # is not palindrome

def main(): # main takes no arguements, instead starts loop and lets palindromes() take an arguement string
    while True:
        string = input("Please type in a palindrome: ")
        if palindromes(string) == True: # palindromes function called to within another function
            print(string, "is a palindrome!")
            return True # can also break, same effect
        else:
            print("that wasn't a palindrome")     

main()