import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
df=load_iris()
x=df.data
y=df.target
#overall flower
plt.scatter(x[:,0],x[:,1])
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

#knn algo
'''from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x,y)
knn.score(x,y)
y_pred=knn.predict([[5.9,3,5.1,1.8]])
y_pred'''

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
knn.score(x_train,y_train)
y_pred=knn.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("accuracy=",accuracy)
