import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
def MarvellousPredictor(path):
    #step 1
    data = pd.read_csv(path)
    print("Dataset loaded sucesfully with the size",len(data))
    
    #prepare data #step 2
    Feature = ["Wether","Temperature"]
    print("Feature names are",Feature)
    
    Wether = data.Wether
    Temperature = data.Temperature
    Play = data.Play
   
    lobj =preprocessing.LabelEncoder() #preprocessing - series to updated series
    #X as of encoded
    WetherX = lobj.fit_transform(Wether)
    TemperatureX = lobj.fit_transform(Temperature)
    Label = lobj.fit_transform(Play)
    
    print("Encoded Whether is ")
    print(WetherX)
    
    print("Encoded Temperature is")
    print(TemperatureX)
    
    Feature = list(zip(WetherX ,TemperatureX)) #list of list thats why typecasting
    #{[0,1],[0,2],[1,2]}
    
    # step 3
    obj = KNeighborsClassifier(n_neighbors = 3)  #training
    obj.fit(Feature,Label)
    # step 4
    output = obj.predict([[0,2]]) #testing
    
    if output == 1:
        print("You can play")
    else:
        print("Dont play")
def main():
    print("____________Marvellous play predictor_______________")
    print("Enter the path of the file which contains dataset")
    path = input()
    
    MarvellousPredictor(path)
    

if __name__ == "__main__":
    main()
    