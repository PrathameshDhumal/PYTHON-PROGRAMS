import pandas as pd

def main():
    data = pd.read_csv("iris.csv")
    print(len(data))
    print(data.head())
    
if __name__ == "__main__":
    main()
