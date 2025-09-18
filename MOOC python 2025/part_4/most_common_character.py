"""Please write a function named most_common_character, which takes a string argument. The function returns the character 
which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which
 appears first in the string should be returned."""

def most_common_character(string):
    helper = 0
    for i in string:
        if string.count(i) > helper: # for iterates through whole string, this checks if the count of the current letter is more than the previous
            helper = string.count(i) # helper acts as the comparison point as the current largest 
            common = i # common changes every time i is more common than the previous characters of the string 
    return common
            
if __name__ == "__main__":
    first_string = "abbbbbeecdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))