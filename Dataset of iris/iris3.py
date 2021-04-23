from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

def main():
    dataset = load_iris()
    
    print("Features of datasets")
    print(dataset.feature_names)

    print("Target names of datasets")
    print(dataset.target_names)
    
    print("Iris data set is:")
  
      
    index =[1,51,101]
    test_target = dataset.target[index]
    test_feature = dataset.data[index]
    
    train_target =np.delete(dataset.target,index)
    train_feature = np.delete(dataset.data,index,axis =0)
    obj = tree.DecisionTreeClassifier()

    
    obj.fit(train_feature, train_target)
    
    result = obj.predict(test_feature)
    print("Result prediction by ML ",result)
    print("Result expected",test_target )
if __name__ == "__main__":
    main()