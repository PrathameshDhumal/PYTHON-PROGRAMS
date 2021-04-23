
#sum of 2 nos with function call
def Addition(value1, value2):  
    ret = value1 + value2  
    return ret
 
def main():
    no1 = int(input("Enter First number"))   
    no2 = int(input("Enter second number"))
    ans = Addition(no1,no2) 
    print("Addition is:",ans)



    no1 = int(input("Enter First number"))   
    no2 = int(input("Enter second number"))
    ans = Addition(no1,no2) 
    print("Addition is : ",ans)
    
#print(__name__)  #special variable name 

if __name__ == "__main__":
    main()