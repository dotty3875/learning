"""Please write a function named anagrams, which takes two strings as arguments. The function returns True if the 
strings are anagrams of each other. Two words are anagrams if they contain exactly the same characters."""

# Write your solution here

def anagrams(string1: str, string2: str): # this hinting is only a hint, not definitive value 
    string1 = sorted(string1) # sorts letters of string for sake of comparison
    string2 = sorted(string2)
    if string1 == string2:
        return True # must return bool, not string "True"
    else: 
        return False

if __name__ == "__main__":
    anagrams("doggy", "ggedy")