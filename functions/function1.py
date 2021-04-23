
#wap:different arguments are used in  thisprograms

#positional arguments
def Student(name,rno,add,marks):
    print("Name is : ",name)
    print("Rollno is :",rno)
    print("Address is :",add)
    print("Marks is:",marks)
#Keyword arguments
def Computer(Ram,Processor,HDD):
    print("RAM size is :",Ram)
    print("Processor name is:",Processor)
    print("HDD size is :",HDD)
   
#default Arguments      (should be form right to left order)
def CircleArea(Radious ,PI=  3.14):
    print("Value of PI is :",PI)
    return PI * Radious * Radious
#variable number of arguments
def Fun(*Value):
    print(type(Value))
    print("number of arguments are :",len(Value))
    



def main():
    Student("Prathamesh",84,"satara road",64)
    Computer(Processor="i7",Ram=8,HDD="1TB")
    Computer(HDD="512gb",Ram=12,Processor="i9")
    CircleArea(10.25)
    CircleArea(Radious=10.25,PI=7.11)
   
    Fun(10,20,30)
    Fun(11,21,51,101)
   
if __name__=="__main__":
    main()
    