#WAP: use of list , perfect number,prime number,even numbers logic in python
class Numbers:

    def __init__(self,no= 10):
        self.size=no
        self.arr= []
    def Accept(self):
        print("enter the elemtents")
        for i in range (self.size):
            print("Enter number: ",i+1)
            self.arr.append(int(input()))
            
            
    def Display(self):  
        print("Elements of list are")
        for i in range (self.size):
            print(self.arr[i])
            
    def Summation(self):
        sum = 0
        for i in range(self.size):
            sum = sum+self.arr[i]
            
        return sum
        
    def EvenDisplay(self):
        print("Even Elements from the list are:")
        for i in range(self.size):
            if (self.arr[i] % 2 ) == 0:
                print(self.arr[i])
                
    def PerfectDisplay(self):
        sum = 0 
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1):
                if (self.arr[i] % j ) == 0 :
                    sum = sum + j 
            if sum ==self.arr[i]: 
                print(self.arr[i])
            sum = 0
            
    def PrimeDisplay(self):
        Flag = False
        for i in range(self.size):
            for j in range(2,int(self.arr[i]/2)+1):
                if(self.arr[i]% j )==0:
                    Flag = True
                    break
                if Flag == False:
                    print(self.arr[i])
                Flag = False
               
            
def main():

    print("enter number of elements")
    value = int (input())
    
    obj1 = Numbers(value)
    obj1.Accept()
    obj1.Display()
    ret = obj1.Summation()
    print("Summation of all elements:",ret)
    obj1.EvenDisplay()
    print("perfect numbers are :")
    obj1.PerfectDisplay()
    
    print("prime numbers are")
    obj1.PrimeDisplay()
if __name__ == "__main__":
    main()