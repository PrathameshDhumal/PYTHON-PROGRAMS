def main():
    no1 = int(input("Enter the first number") )
    no2 = int(input("Enter the second number") )
    try:
        ans = no1 / no2
        
    except Exception as eobj:
        print("Exception occurs ",eobj)
        
    else:
        print("Division is:",ans)
        
    finally:
        print("Deallocate all the resources")
if __name__ == "__main__":
    main()