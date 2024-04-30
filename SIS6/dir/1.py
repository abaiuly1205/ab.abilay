import os 
   
path = os.getcwd() 

#print files and directories
print("Files and directories in '", path, "' :")  
with os.scandir(path) as it:
    for x in it: 
            print(x.name)
            
#print directories
print("Directories:") 
with os.scandir(path) as it:
    for entry in it: 
        if entry.is_dir():
            print(entry.name)

#print files
print("Files:")   
with os.scandir(path) as it:
    for entry in it: 
        if not entry.is_dir():
            print(entry.name)