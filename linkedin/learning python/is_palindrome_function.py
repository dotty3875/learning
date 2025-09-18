def is_palindrome(teststr):
    teststr = teststr.lower()
    stringCheck = ""
    for i in teststr:
        if i.isalnum() == True: # checks if alphanumeric (e.g. abc123) and filters out spaces, commas, exclamation marks, etc.
            stringCheck += i
            
    if stringCheck == stringCheck[::-1]: # checks if palindrome 
        return True
    else:    
        return False

# test_word = "Madam, I'm Adam."
# test_word = "RACE CAR!"
# test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"