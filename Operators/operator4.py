class Student:
    def __init__(self,str,a,b,c):
        self.name = str
        self.m1=a
        self.m2=b
        self.m3=c
        
    def __eq__(self,other):
        if ((self.m1==other.m1) and (self.m2 == other.m2) and (self.m3 == other.m3)):
            return True
        else:
            return False
            
    def __gt__(self,other):
        if ((self.m1>other.m1) and (self.m2>other.m2) and (self.m3>other.m3)):
            return True
        else:
            return False
    

def main():
    obj1 = Student("Prathamesh",99,99,100)
    obj2 = Student("Om",70,80,98)
    
    if obj1 == obj2:
        print("Both are equal")
    else:
        print("Both are not equal")
        
    if obj1>obj2:
        print("obj1 is greater")
    else:
        print("second object is greater")
        

if __name__ == "__main__":
    main()
    