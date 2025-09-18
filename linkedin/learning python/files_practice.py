
sampleFile = open("sampleFile.txt", "w+") # the + next to w means if it doesnt exist, create it. w - write
sampleFile.write("Sample text") # writes to file
sampleFile.close() # closes file

sampleFile = open("sampleFile.txt", "a+") # a - append (adds instead of overwriting)
sampleFile.write("\nSample text 2")
sampleFile.close()

sampleFile = open("sampleFile.txt", "r") # r - read (cannot write to/append)
if sampleFile.mode == "r": # checks if its open for reading
     print(sampleFile.read())

fileLines = sampleFile.readlines() # readlines() is used to output line by line
for i in fileLines:
    print(i)