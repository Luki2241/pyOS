import os
import sys
from settings import OS_USER, OS_PL
import hashlib
def createuser():
    filename = OS_PL
    filepath = os.path.join(OS_USER, filename)
    name = input("Enter your name: ").lower()
    password = input("Enter a password: ")
    conf_password = input("Confirm password: ")
    if conf_password != password:
        print("Password is not same as above! \n")
    enc = password.encode("utf-8")
    hash1 = hashlib.md5(enc).hexdigest()
    with open(filepath, "w") as f:
        f.write(name + "\n")
        f.write(hash1)
        
def login():
    filename = OS_PL
    filepath = os.path.join(OS_USER, filename)
    name = input("Enter name: ").lower()
    password = input("Enter password: ")
    
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open(filepath, "r") as f:
        stored_name, stored_password = f.read().split("\n")
        if name == stored_name and auth_hash == stored_password:
            print("Logged in Successfully!")
            global logged_user
            logged_user = name
            return True
        else:
            print("Login failed! \n")       