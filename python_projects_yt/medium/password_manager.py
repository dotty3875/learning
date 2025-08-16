############################################################################################################################################################
#THE MASTER PASSWORD FEATURE IS MOSTLY BROKEN DUE TO THE TUTORIAL BEING RUSHED AND NOT COVERING HOW TO PROPERLY IMPORT FERNET
#i've added the correct import base os so on so forth that he didnt
#to be functional code, i need to remove the master password feature which is ridicilous as its a crucial part of the code
#or i go into it myself, frankly i dont care right now but this is still a good example of what a password manager can do if it were configured correctly
############################################################################################################################################################




import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#pip install cryptography to access this

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ") 
key = load_key() + master_pwd.encode() #encode needed to convert to bytes since key is bytes
fer = Fernet(key)

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() '''#this is commented out because it is single use to generate key.key with the chosen master password


def view(): 
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #will strip a linebreak 
            user, passw, = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()))


def add():
    name = input('Account name: ')
    pwd = input('Password: ')

#when using open(text.txt, 'a') the a is defining something, in this case a is for writing, r is for reading, w is to create (w will wipe out the file each time to 0 when creating)
#make sure to sperate the document from the opening mode or it will consider it to be like text.txta instead of text.txt + a opening mode
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + fer.encrypt(pwd.encode()).decode() + "\n") #\n is a line break, the fer.encrypt stuff encodes the passwords 

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add)? press q to quit ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add": 
        add()
    else:
        print("invalid mode.")
        continue