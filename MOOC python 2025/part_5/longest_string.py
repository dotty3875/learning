"""Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list.
 You may assume there is always a single longest string in the list."""

# Write your solution here
def longest(string: list):
    longest = ""
    for i in string:
        if len(i) >= len(longest): # compares length of i longest and updates longest to i if i is larger
            longest = i
    
    return longest 


if __name__ == "__main__":
    strings = ["first", "second", "third"]
    print(longest(strings))