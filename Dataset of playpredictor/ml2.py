
import numpy as np
from sklearn.metrics
import r2_score


def MarvellousPredictor():
    X = [1,2,3,4,5]#X
    Y = [3,4,2,4,5]#Y
    
    X_Mean=np.mean(X)#x bar
    Y_Mean=np.mean(Y)#y bar 
    
    Numerator = 0
    Denomenator = 0
    for i in range(len(X)):
        Numerator = Numerator + ((X[i] - X_Mean)*(Y[i] - Y_Mean))
        Denomenator = Denomenator + ((X[i]- X_Mean)**2)
        
    m = Numerator/Denomenator
    
    print("Values of X:",X)
    print("Values of Y:",Y)
    
    print("Value of m:",m)
    
    c = Y_Mean - (m * X_Mean)
    print("Value of c:",c)
    
    Numerator =0
    Denomenator = 0
    for i in range(len(X)):
        Numerator = Numerator + (((m*X[i] + c)-Y_Mean)**2)
        Denomenator = Denomenator + ((Y[i]- Y_Mean)**2)
    RSquare = Numerator/Denomenator
    print("Value of R2 is:",RSquare) 
    
    
    
def main():
 
    MarvellousPredictor()
    

if __name__ == "__main__":
    main()
    