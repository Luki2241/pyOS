import commands
import user
baseCommands = ["clear", "help", "exit"]
fileCommands = ["ls","cat", "touch", "rm", "rmdir", "edit", "mkdir"]
naviCommands = ["cd", "pwd"]
sysCommands = ["time", "whoami", "neofetch", "edsys", "logout"]
def shell():
    while True:
        cmd = input(f"{user.logged_user}@pyOS> ").strip().lower()
        #base commands
        
        if cmd == baseCommands[0]:
            commands.clear()
            
        elif cmd == baseCommands[1]:
            commands.help()
            
        elif cmd == baseCommands[2]:
            commands.exitpy()
            
        #file commands   
         
        elif cmd == fileCommands[0]:
            commands.ls()
            
        elif cmd == fileCommands[1]:
            commands.cat()
            
        elif cmd == fileCommands[2]:
            commands.touch()
            
        elif cmd == fileCommands[3]:
            commands.rm()
            
        elif cmd == fileCommands[4]:
            commands.rmdir()
        
        elif cmd == fileCommands[5]:
            commands.edit()
            
        elif cmd == fileCommands[6]:
            commands.mkdir()
            
        #navigation commands  
          
        elif cmd == naviCommands[0]:
            commands.cd()
        
        elif cmd == naviCommands[1]:
            commands.pwd()
            
        #sys commands
            
        elif cmd == sysCommands[0]:
            commands.time()
        
        elif cmd == sysCommands[1]:
            print(f"The current user is: {user.logged_user}")
        
        elif cmd == sysCommands[2]:
            commands.neofetch()
        
        elif cmd == sysCommands[3]:
            commands.edsys()
            
        elif cmd == sysCommands[4]:
            print("Logging out...")
            break
        
        else:
            print("Command not found! Type help to see all commands!")