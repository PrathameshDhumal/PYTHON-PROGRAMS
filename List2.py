#WAP: List in for loop
def Display(LIST):
    icnt = 0
    for icnt in range(len(LIST)):
        print(LIST[icnt])

def main():
    Arr = [10,20,30,40,50]
    Display(Arr)
    
if __name__ == "__main__":
    main()
