#WAP: use of for loop in python

def DisplayF(value):
    print("o/p of For LOOp")
    icnt = 0
    for icnt in  range (0,value):
        print("Jay Ganesh")

def DisplayW(value):
    print("o/p for whle loop")
    icnt = 0
    while icnt <value:
        print("Jay ganesh")
        icnt = icnt +1
        
def main():
    print("ENter the number of iterations")
    no = int(input())
    
    
    DisplayF(no)
    DisplayW(no)
    
 
if __name__ == "__main__":
    main()