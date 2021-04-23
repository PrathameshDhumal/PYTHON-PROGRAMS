#WAP: selection

import marvellousnumber as MN
#from  marvellousnumber import even
#
def main():
    print("Enter the number ")
    value =  int(input())
    
    
    
    bret = MN.even(value)
    if bret == True:
        print("{} is Even number ".format(value))
    else:
        print("{} is Odd number ".format(value))
        
if __name__ == "__main__":
    main()
    
    
    
    