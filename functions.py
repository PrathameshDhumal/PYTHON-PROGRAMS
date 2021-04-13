
#1.Function which accepts nothing and returns nothing 
def fun():                  
    print("Function fun")
    
#2.Function which accepts parameter and returns nothing 
def gun(no):
    print("Function gun with parameter",no)
#3.Function which accepts parameter and returns nothing   
def sun(no):
    print("Function sun with parameter",no) 
    return no+1
    
#4. Function Accepts multiple values and return multiple values    
def AddSub(no1,no2):
    add = no1+no2
    sub = no1-no2
    return add,sub
    
#5. Nested function definition
def Marvellous():
    print("Inside Marvellous")
    def Infosystems():
        print("Inside Infosystems")
    Infosystems()    

    
def main():                     
    fun()
    gun(11)
    ret = sun(20)
    print("return value of sun :",ret)
    
    ret1,ret2= AddSub(10,8)
    print("Addition is : ",ret1)
    print("Substraction is :", ret2)
    
    Marvellous()
if __name__ == "__main__":
    main()