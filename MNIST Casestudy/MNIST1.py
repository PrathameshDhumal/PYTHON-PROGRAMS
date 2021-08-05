#############################################################
#
#Author:Prathamesh Dhumal
#Date:1/7/21
#About:Finding Accuracy of MNIST casestudy using Decision Tree Classifier.
#
##############################################################
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('mnist.csv')

df_x = data.iloc[:,1:]  # Labels
df_y = data.iloc[:,0]   # Pixels

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

#descision tree
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

print("Testing accuracy using decision tree classifier : ",dt.score(x_test,y_test) * 100)

print("Training accuracy using decision tree classifier : ",dt.score(x_train,y_train) * 100)

