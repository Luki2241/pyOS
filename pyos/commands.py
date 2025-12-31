import os
import datetime
import time as tm
from settings import OS_ROOT, OS_NAME, BOOT_TIME
import filesystem
baseCommands = ["clear", "help", "exit"]
fileCommands = ["ls","cat", "touch", "rm", "rmdir", "edit", "mkdir"]
naviCommands = ["cd", "pwd"]
sysCommands = ["time", "whoami", "neofetch", "edsys", "logout"]
#uptime
def cmd_uptime():
    uptime = int(tm.time() - BOOT_TIME)

    seconds = uptime % 60
    minutes = (uptime // 60) % 60
    hours   = (uptime // 3600) % 24
    days    = uptime // 86400

    if days > 0:
        print(f"Uptime: {days}d {hours}h {minutes}m")
    elif hours > 0:
        print(f"Uptime: {hours}h {minutes}m")
    elif minutes > 0:
        print(f"Uptime: {minutes}m {seconds}s")
    else:
        print(f"Uptime: {seconds}s")
#base commands
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def help():
    print("""
Available commands:  
help        -show this help
clear       -clear the shell
exit        -exit pyOS
ls          -list all files and folder
touch       -creates file
cat         -opens file
rm          -deletes file
rmdir       -deletes folders
edit        -opens the text editor
mkdir       -creates a folder
cd          -change directory
pwd         -shows current directory
time        -shows date and time
whoami      -shows current user
neofetch    -shows infos about the system
echo        -prints a message to the screen 
edsys       -change systems name
logout      -logs the user out        
          """)
    
def exitpy():
    print("Shutting down pyOS...")
    quit()
#filesystem commands
def ls():
    filesystem.listdirectory()

def touch():
    filesystem.createfile()

def cat():
    filesystem.openfile()
    
def rm():
    filesystem.deletefile()
    
def rmdir():
    filesystem.deletefolder()
    
def edit():
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
    
def mkdir():
    filesystem.makedir()
    
#navigation commands    

def cd():
    foldername = input("Enter directory name to change to(case-sensitive): ")
    folderpath = os.path.join(OS_ROOT, foldername)
    try:
        os.chdir(folderpath)
        newdir = os.getcwd()
        print(f"Directory changed to: {newdir}")
    except FileNotFoundError:
        print(f"Directory not found: {newdir}")
    
def pwd():
    currentdir = os.getcwd()
    print(f"The current directory is: {currentdir}")
    
#sys commands

def time():
    x = datetime.datetime.now()
    print(x)
    
def neofetch():
    print(f"OS: {OS_NAME}")
    print("Shell: pyOSshell 1.0")
    cmd_uptime()
    
def edsys():
    global OS_NAME 
    OS_NAME = input("Enter new system name: ")
    print(f"System name changed to: {OS_NAME}")
    
