import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MeanData(arr):
    size = len(arr)
    sum = 0
    
    for i in range(size):
        sum =sum+arr[i]
    
    return (sum/size)
def MarvellousHeadBrain(Name):
    dataset = pd.read_csv(Name)
    print("Size of our dataset is",dataset.shape)  #pandas method shape
    
    X = dataset["Head Size(cm^3)"].values
    Y = dataset["Brain Weight(grams)"].values
    
    print("Length of X",len(X))
    print("Length of Y",len(Y))
    
    Mean_X = MeanData(X)
    Mean_Y = MeanData(Y)
    
    print("Mean of Independant variable is ",Mean_X)
    print("Mean of Independant variable is ",Mean_Y)
    Numerator = 0
    Denomenator = 0
    
    for i in range(len(X)):
        Numerator = Numerator + (X[i] - Mean_X) * (Y[i] - Mean_Y)
        
        Denomenator = Denomenator + (X[i] - Mean_X)**2
    m = Numerator / Denomenator
    print("Value of slope M is ",m)
     #Y = mx+c   formula
    #c =Y - mx   formula
    c= Mean_Y - (m*Mean_X)
    print("Value of Y intercept is :",c)
    
    X_Start = np.min(X) - 200
    X_End = np.max(X) + 200
   
    x = np.linspace(X_Start,X_End)#100 100 100
    y = m*x + c 

    plt.plot(x,y,color = 'r', label = "Line of Regression") #notation
    plt.scatter(X,Y,color = 'b', label = "Data plot")   #notation
   
    plt.xlabel("Head size") #down label 
    
    plt.ylabel("Brain Weight") #side    label
   
    plt.legend()#actual line disti
    plt.show()#points distat
    # r2 calculation
def main():
   # print("Enter file name of dataset")
    #name = input()
    
    MarvellousHeadBrain("MarvellousHeadBrain.csv")
    
if __name__ == "__main__":
    main()