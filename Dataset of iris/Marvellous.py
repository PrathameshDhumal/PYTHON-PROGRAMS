from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

def CalculateDistance(X,Y):
    return distance.euclidean(X,Y)
    
class Marvellous():
    def fit(self,TrainingData, TrainingTarget):
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget
        
    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.Shortest(row)
            predictions.append(label)
        return predictions
        
    def Shortest(self,row):
        Minindex = 0
        MinDistance = CalculateDistance(row,self.TrainingData[0])
        
        for i in range(1,len(self.TrainingData)):
            Distance = CalculateDistance(row,self.TrainingData[i])
            if Distance < MinDistance:
                MinDistance = Distance
                Minindex = i
        return self.TrainingTarget[Minindex]
        
def MarvellousKNN():
    Line = "*"*50
    iris = load_iris()      # 150 / 5
        
    data = iris.data        # 150 /4
    target = iris.target    # 150 / 1
    
    print(Line)
    print("Actual Dataset")
    print(Line)
    for i in range(len(iris.target)):
        print("ID : %d Feature : %s, Label : %s" %(i,iris.data[i], iris.target[i]))
#  75/4           75/4          75/1          75/1
    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5)
    
    print(Line)
    print("Training Data set")
    print(Line)
    for i in range(len(data_train)):
        print("ID : %d Feature : %s, Label : %s" %(i,data_train[i], target_train[i]))
            
    print(Line)
    print("Testing Data set")
    print(Line)
    for i in range(len(data_test)):
        print("ID : %d Feature : %s, Lebel : %s" %(i,data_test[i], target_test[i]))
    
    print(Line)
    mobj = Marvellous()     # Marvellous(5)
    
    mobj.fit(data_train,target_train)
  
    ret = mobj.predict(data_test)       #  2  75/4
    
    print("Result of Machine Learning Model")
    print(Line)
    for i in range(len(data_test)):
        print("ID : %d Expectation : %s, Prediction : %s" %(i, target_test[i],ret[i]))
    print(Line)

    icnt = 0
    for i in range(len(data_test)):
        if target_test[i] != ret[i]:
            icnt = icnt + 1
    print("Number of wrong answers by the ML model : ",icnt)
    print(Line)
    
    Accuracy = accuracy_score(target_test,ret)
    return Accuracy
    
def main():
    ret = MarvellousKNN()
    print("Accuracy of KNN is : ",ret*100,"%")
    print("*"*50)
    
if __name__ == "__main__":
    main()
