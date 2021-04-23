#WAP: terative approach in python
#Iterative Approach  
def startDynamic(No,message):
    iCnt = 0
    while iCnt<No:
        print(message)
        iCnt =  iCnt + 1
        
        


def main():
    print("Enter number of times you want too display message on screen")
    value = int(input())
    print("Enter the message")
    name =  int(input())
    startDynamic(value,name)
if __name__ == "__main__":
    main()