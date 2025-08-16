"""Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt."""

# Write your solution here
string = "a"
while string != "":
    string = input("Please type in a string: ")
    print(string)
    print(f"-"* len(string))
