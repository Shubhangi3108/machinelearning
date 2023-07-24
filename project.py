import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Play.csv')
x=df.iloc[:,1:-1].values
y=df.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
for i in range(4):
    x[:,i]=lab.fit_transform(x[:,i])
    print(lab.classes_)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
accuracy=accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion matrix")
print(confusion_matrix(y_test, y_pred))