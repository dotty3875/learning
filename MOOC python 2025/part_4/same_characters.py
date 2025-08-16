"""Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. 
The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls 
outside the scope of the string, the function returns False."""

# Write your solution here
def same_chars(string, index1, index2):
    if index1 >= len(string) or index2 >= len(string): # required to prevent "string index out of range" error
        return False
    elif string[index1] == string[index2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))