#WAP: Addition of two nos using format
def Addition(no1,no2):
 

    return no1+no2
 
def main():
    value1 = int(input("Enter First number"))
    value2 = int(input("Enter second number"))
    
    ret = Addition(value1,value2)
    
    print("Addition of {} and {} is {} ".format(value1,value2,ret))
    
if __name__ == "__main__":
    main()