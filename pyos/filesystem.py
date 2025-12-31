import os
import shutil

def createfile():
        filename = input("Enter a name for your file (only txt files, include .txt): ").lower()
        filepath = os.path.join(os.getcwd(), filename)
        try:
            with open(filepath, "x") as f:
                print("File has been created!")
        except FileExistsError:
            print("File already exists.")
            
def openfile():
    filename = input("Enter the file to open: ").lower()
    filepath = os.path.join(os.getcwd(), filename)
    try:
        with open(filepath, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found! Please check the file name.")
    
def deletefile():
    filename = input("Enter the file to remove: ").lower()
    filepath = os.path.join(os.getcwd(), filename)
    try:
        os.remove(filepath)
        print("File has been deleted!")
    except FileNotFoundError:
        print("File not found! Please check the file name.")
        
def renamefile():
    old_name = input("Enter file to rename: ").lower()
    new_name = input("Enter the new name: ").lower()

    old_path = os.path.join(os.getcwd(), old_name)
    new_path = os.path.join(os.getcwd(), new_name)

    try:
        os.rename(old_path, new_path)
        print("File renamed successfully!")
    except FileNotFoundError:
        print("File not found! Please check the file name.")
        
def texteditor():
    filename = input("Enter the file to modify or write to (include .txt): ").lower()
    filepath = os.path.join(os.getcwd(), filename)

    buffer = []

    print("pyTextedit")
    print("Type :q to quit without saving")
    print("Type :wq to quit and save")
    print("----------------")

    while True:
        line = input()

        if line == ":q":
            print("Exiting editor...")
            break

        elif line == ":wq":
            if buffer:
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write("\n".join(buffer) + "\n")
            print("Saved and exited.")
            break

        else:
            buffer.append(line)
    
def listdirectory():
    print(os.listdir(os.getcwd()))

def makedir():
    foldername = input("Enter a folder name: ").lower()
    folderpath = os.path.join(os.getcwd(), foldername)
    try:
        os.mkdir(folderpath)
    except FileExistsError:
        print("Folder already exists!")

def deletefolder():
    foldername = input("Enter the folder to remove: ").lower()
    folderpath = os.path.join(os.getcwd(), foldername)
    try:
        shutil.rmtree(folderpath)
        print("Folder has been deleted!")
    except FileNotFoundError:
        print("Folder not found! Please check the file name.")

