"""Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text,
 the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. 
 If the second argument is an empty string, the line should consist of stars."""

def line(num, word):
    if word == "":  
        word = "*" # replaces with stars if no characters in the word
    print(num * word[0:1])

if __name__ == "__main__": # required for the course exercise tester, otherwise call function normally
    line(3, "")