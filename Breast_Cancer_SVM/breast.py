
##############################################################
#
#Author:Prathamesh Dhumal
#Date:18/7/21
#About:Breast cancer dataset using Support Vector Machine
#
##############################################################
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def MarvellousSVM():
    #load Dataset
    cancer = datasets.load_breast_cancer()
    
    #Print The names of the 13 Features
    print("Features of the cancer datasets:",cancer.feature_names)

    #Print the Label type of Cancer('maligant' 'benign')
    print("Labels of the cancer datasets:",cancer.target_names)

    #print data(feature)shape
    print("Shape of datasets is:",cancer.data.shape)

    #print the cancer data features(top 5 records)
    print("First 5 records are: ")
    print(cancer.data[0:5])
    
    #Print the cancer labels(0:maligant,1:benign)
    print("Target of datasets:",cancer.target)

    #Split the datset into training set and test set
    X_train,X_test,y_train,y_test=train_test_split(cancer.data, cancer.target,test_size=0.3,random_state =109)
    #70% training and 30% testing

    #Create a svm classifier
    clf =svm.SVC(kernel ='linear') #linear Kernel

    #Train the model using the training sets
    clf.fit(X_train,y_train)

    #predict the responce for test datasets
    y_pred=clf.predict(X_test)
    
    #Model Accuracy : How often is the classifier Correct?
    print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred)*100)

def main():
    print("_________________Breast cancer dataset using Support Vector Machine______________")
    MarvellousSVM()

if __name__ == "__main__":
    main()