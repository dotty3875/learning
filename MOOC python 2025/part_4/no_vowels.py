"""Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be 
the same as the original but with all vowels removed.

You can assume the string will contain only characters from the lowercase English alphabet a...z."""

def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"] # vowels used to compare to later
    for i in string: # iterates each character of string - each character is checked
        for i in vowels: # iterates through each letter in vowels
            if i in string: # checks current character against current vowel from vowel list 
                string = string.replace(i, "") # replaces detected vowel with an empty space
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))