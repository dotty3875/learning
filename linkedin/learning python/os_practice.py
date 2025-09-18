import os, time
from os import path
from datetime import datetime

print(os.name) # prints the operating system type. "nt" (new technology) is Windows, "posix" is linux and macOS, "java" for jython

print("Item exists:", path.exists("sampleFile.txt")) # checks if the item exists - true/false
print("Item is a file:", path.isfile("sampleFile.txt")) # checks if its a file - true/false
print("Item is a directory:", path.isdir("sampleFile.txt")) # checks if it's a directory - true/false

print("Item's path:", path.realpath("sampleFile.txt")) # full file path of item
print("Item's path and name:", path.split(path.realpath("sampleFile.txt"))) # full file path of item but splits the file name and it's path
 
lastModified = time.ctime(path.getmtime("sampleFile.txt")) # checks last modification time
print(lastModified)
print(datetime.fromtimestamp(path.getmtime("sampleFile.txt"))) # date time object for last modification time using timestamp

td = datetime.now() - datetime.fromtimestamp(path.getmtime("sampleFile.txt")) # the time difference between now and the last time it was modified - is an object not float
print(f"it has been {td} since last modification") # prints time differences between now and modification time
print(f"or {td.total_seconds()} seconds") # .total_seconds() converts the td object to show its full time only in seconds