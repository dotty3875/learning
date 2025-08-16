"""Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish."""




sentence = "" # empty string is good for storing str 
last = ""
while True:
    word = str(input("Please type in a word: ")) 
   
    if word == "end" or word == last:
        break
    sentence += word + " " #this adds the words all together in the sentence with the += and the " " adds a space 
    last = word #this turns the latest word into the "last" variable and the above means it will break if the new word is the same as the last
print(sentence) 