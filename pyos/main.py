from settings import OS_ROOT, OS_USER
import os
from user import login, createuser
from shell import shell
#creates root folder
def init_os():
    if not os.path.exists(OS_ROOT):
        os.mkdir(OS_ROOT)
        print("OS folder created!")
    if not os.path.exists(OS_USER):
        os.mkdir(OS_USER)
        print("User folder created!")

def main():
    init_os()
    while True:
        print(""" 
--- pyOS login system --- 
1. Create user              
2. Login
3. Exit and shutdown pyOS              
              """)
        try:
            option = int(input("Enter an option: "))
        
            if option == 1:
                createuser()
                
            elif option == 2:
                if login():
                   shell()
                    
            elif option == 3:
                print("Shutting down pyOS...")
                break
                
            else:
                print("Invalid option.")
                
        except ValueError:
            print("Invalid option.")
    
if __name__ == "__main__":
    main()