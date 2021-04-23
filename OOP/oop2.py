class Student:
    School = "Podar"
   
    def __init__(self,no1,no2,no3):
        self.m1=no1
        self.m2=no2
        self.m3=no3
        
    def Instance_Total(self):
        print("Inside Instance method")
        return self.m1+self.m2+self.m3
    @classmethod   
    def Class_DisplaySchool(cls): #cls - for class method
        print("School name is :",cls.School)
        
        
def main():
    Student.Class_DisplaySchool()
    obj1 = Student(50,60,70)
    obj2 = Student(80,90,77)
    ret = obj1.Instance_Total()
    print("Total marks ",ret)
    ret = obj2.Instance_Total()
    print("Total marks ",ret)
    

if __name__ == "__main__":
    main()