from os import path
import os


def file_info():
    totalByte = 0 # keeps track of total bytes
    tester = (path.realpath("tester")) # gets full file path of "tester" directory
    for i in os.listdir(tester): # for each file present in "tester" directory, loop through
        if i[-4:] == ".txt": # if it ends in ".txt" meaning filters for text documents
            totalByte += os.path.getsize(os.path.join(tester, i)) # the os.path.getsize() looks for byte size of a specified file, and the os.path.join(tester, i) connects file path (tester) to the file name (i) as a workable object to get bytes from

    return totalByte

result = file_info()
print(result)