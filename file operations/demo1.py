def main():
    name = input("Enter the file name that you want to create")
    
    fobj = open(name,"w")
    
    str  = input ("enter the data that wwe want to write in the file")
    fobj.write(str)
if __name__ == "__main__":
    main()