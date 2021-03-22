''' 
Name: Christopher Nilo A. Caysido
'''
from recursive import recursiveFunc

def main():
    print("This is when a directory is given as an argument")
    path_dir = "Mod1_PE01/recursive"
    recursiveFunc(path_dir)
    
    print("This is when a file is given as an argument")
    path_file = "Mod1_PE01/recursive/number1.txt"
    recursiveFunc(path_file)

if __name__ == "__main__":
    main()
    
