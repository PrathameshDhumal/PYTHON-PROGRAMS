class AgeInvalid(Exception):
    def __init__(self,data):
        self.data = data
        

def main():
    try:
        age = int(input("Enter your age for pan card")) 
        if age<18:
            raise AgeInvalid("Your age is less than 18")
        
    except AgeInvalid as obj:
        print(obj)
        
    else:
        print("You will get your pan card within 7 days")
if __name__ == "__main__":
    main()