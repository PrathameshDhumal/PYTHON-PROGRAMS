import sys

def main():
    print("Recurion limit is : ",sys.getrecursionlimit())
    
    sys.setrecursionlimit(150000000)
    
    print("New Recurion limit is : ",sys.getrecursionlimit())
    
if __name__ == "__main__":
    main()
