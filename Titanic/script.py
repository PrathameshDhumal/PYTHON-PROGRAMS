##############################################################
#
#Author:Prathamesh Dhumal
#Date:22/7/21
#About:Logistic regression on Titanic Dataset
#
##############################################################

import math 
import numpy as np
import pandas as pd 
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitaticLogistic():
    #step 1 :Load data
    titanic_data = pd.read_csv('MarvellousTitanicDataset.csv')

    print("First 5 entries from the dataset")
    print(titanic_data.head())

    print("Number of passengers are: "+str(len(titanic_data)))

    #step 2 :Analyze data
    print("Visualization : Survived and Non Survived passengers")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target).set_title("Survived and Non Survived passengers")
    show()

    print("Visualization : Survived and Non Survived passengers based on Gender")
    figure()
    target ="Survived"

    countplot(data=titanic_data,x=target,hue ="Sex").set_title("Survived and Non Survived passengers based on Gender")
    show()

    print("Visualization : Survived and Non Survived passengers based on Passenger class")
    figure()
    target ="Survived"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("Survived and Non Survived passengers based on Passenger class")
    show()

    print("Visualization : Survived and Non Survived passengers based on Age")
    figure()

    titanic_data["Age"].plot.hist().set_title("Survived and Non Survived passengers based on Age")
    show()

    print("Visualization : Survived and Non Survived passengers based on Fare")
    figure()
    target ="Survived"

    titanic_data["Fare"].plot.hist().set_title("Survived and Non Survived passengers based on Fare")
    show()

    #Step 3 :Data cleaning
    titanic_data.drop("zero",axis = 1 , inplace= True)

    print("First 5 entries from the loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"] , drop_first =True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first = True)
    print(Pclass.head(5))

    print("Values of dataset after concatenating new columns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis =1)
    print(titanic_data.head(5))

    print("Values of dataset after removing irrelevant columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis =1,inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived",axis = 1)
    y = titanic_data["Survived"]

    #step 4: Data Training
    X_train ,X_test ,y_train ,y_test = train_test_split(x,y,test_size =0.5)

    logmodel =LogisticRegression()

    logmodel.fit(X_train,y_train)

    #step 5: Data testing 
    Prediction = logmodel.predict(X_test)

    #step 6: Calculate Accuracy
    print("Classification report of Logistic Regression is : ")
    print(classification_report(y_test,Prediction))

    print("Confusion matrix of Logistic Regression is: ")
    print(confusion_matrix(y_test,Prediction))

    print("Accuracy of Logistic Regression is: ")
    print(accuracy_score(y_test,Prediction)*100)

def main():
    print("__________________Supervised Machine Learning_________________")
    print("______________Logistic Regression on Titanic Dataset__________")
    TitaticLogistic()
if __name__ == "__main__":
    main()
