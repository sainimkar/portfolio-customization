import numpy as np
from numpy import genfromtxt
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
records = genfromtxt(r'C:\se_project\training_data.txt', delimiter=',',dtype=float)
x_axis = []
y_axis = []
unknown = np.array([[20,2,17731,0,14184.8],[33,4,55311,0,33186.6],[26,2,56410,26342.93,18785.07],[27,2,47000,21115.63103,16484.36897],[23,4,94611,11705.5136,45061.0864],[38,0,33955,4047.679342,29907.32066]])
# training data
# X = features
X = records[:,range(0,5)]
#print(X)
# Y = target class
Y = records[:,5]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=100)
Y_train = Y_train.ravel()
Y_test = Y_test.ravel()
for k in range(0,20):
    K_value = k + 1
    neighbor = KNeighborsClassifier(n_neighbors = K_value)
    neighbor.fit(X_train, Y_train)
    y_pred = neighbor.predict(X_test)
    #print(neigh.score(X_test, Y_test))
    #print ("Accuracy is ", accuracy_score(Y_test,y_pred) * 100,"for K-Value:",K_value)
    x_axis.append(K_value)
    y_axis.append(accuracy_score(Y_test,y_pred) * 100)
    if(k == 3):
        unknown_pred = neighbor.predict(unknown)
        print(unknown_pred)
plt.title('Accuracy over K')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.plot(x_axis,y_axis)
plt.show()