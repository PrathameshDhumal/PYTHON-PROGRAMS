##############################################################
#
#Author:Prathamesh Dhumal
#Date:18/7/21
#About: Diabetes Predictor application using K nearest neighbour algorithm
#
##############################################################
#Import the Libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

print("____________Diabetes Predictor using K Nearest Neighbor_____________")
#Read the Dataset
diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data: {}".format(diabetes.shape))
#Split the dataset
X_train,X_test,y_train,y_test =train_test_split(diabetes.loc[:,diabetes.columns
!='Outcome'],diabetes['Outcome'],stratify = diabetes['Outcome'],random_state=66)

training_accuracy = []
test_accuracy =[]

#try n-neighbors from 1 to 10
neighbors_settings = range(1,11)

for n_neighbors in neighbors_settings:
    #Build the Model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train,y_train)

    #Record training set accuracy
    training_accuracy.append(knn.score(X_train,y_train))

    #Record test set accuracy
    test_accuracy.append(knn.score(X_test,y_test))

#Plot the output for better understanding
plt.plot(neighbors_settings,training_accuracy,label="training accuracy")
plt.plot(neighbors_settings,test_accuracy,label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig("knn_compare_model")
plt.show()

knn=KNeighborsClassifier(n_neighbors=9)

knn.fit(X_train,y_train)
#Print the accuracy of the dataset
print('Accuracy of KNN classifier on training set : {:.2f}'.format(knn.score(X_train,y_train)*100))

print('Accuracy of KNN classifier on test set : {:.2f}'.format(knn.score(X_test,y_test)*100))


