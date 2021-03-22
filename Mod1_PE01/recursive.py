
'''
Write a recursive function that expects a pathname as an argument. 
The path- name can be either the name of a file or the name of a directory. 
If the pathname refers to a file, its name is displayed, 
followed by its contents. Otherwise, if the pathname refers to a directory, 
the function is applied to each name in the directory. 
Test this function in a new program.

Name: Christopher Nilo Caysido
'''
import os
def recursiveFunc(path):
    if os.path.isdir(path): #If argument is a directory
        files = os.listdir(path) #Make a list of the files within a path
        dirName = os.path.basename(path)
        for i in range(0,len(files)):
                files[i] = path +"/"+ files[i]
        for item in files: #Then for every file or directory
            print("Directory: " + dirName + "\n")
            recursiveFunc(item) #recursively call the recursive function
    elif os.path.isfile(path): #else
        file_read = open(path,'r') # Create a file read variable
        file_name = os.path.basename(path)
        print("File Name: "+file_name + "\n" + "Content: " + "\n")
        print(file_read.read()+"\n") # Print the contents
    else: 
        print("The argument entered is neither a directory or a path try again")
