class Marvellous:               #class
    value1 = 11
    
    def __init__(self,no1,no2):  #constructor
        self.i = no1            #instance
        self.j = no2
        print("Inside Constructor")
    def __del__(self):
        print("Inside Destructor")
        
    def Fun(self):
        print("Inside Fun method")
        print("Value of J is ",self.j)
        
def main():
    obj1 = Marvellous(11,21)
    obj2 = Marvellous(51,101)
    
    print("value of i from obj1",obj1.i)
    print("Value of i from obj2",obj2.i)
    print("Value of Class member ", Marvellous.value1)
    obj1.Fun()
    obj2.Fun()
    del obj1
    del obj2
    
if __name__ == "__main__":
    main()