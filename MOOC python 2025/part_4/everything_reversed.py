"""Please write a function named everything_reversed, which takes a list of strings as its argument. The function 
returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list."""

def everything_reversed(list):
    reversedList = []
    for i in list:
        reversedList.append(i[::-1]) # [::-1] goes through each string backwards
    return reversedList[::-1] # returns the list of reversed strings in reverse, "hi" being last instead of first
        
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)