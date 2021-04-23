def main():
    name = input("Enter the file name that you want to create")
    
    fobj = open(name,"r")
    
    print("Data from file is ")
    print(fobj.read())
if __name__ == "__main__":
    main()