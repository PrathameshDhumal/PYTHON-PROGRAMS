#WAP:  addition of list
def Addition(LIST):
    icnt = 0
    sum = 0
    for icnt in range(len(LIST)):
        sum = sum + LIST[icnt]
    return sum

def main():
    Arr = [10,20,30,40,50]
    ret = Addition(Arr)
    print("Addition is :",ret)
    
if __name__ == "__main__":
    main()
