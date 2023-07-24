import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Play.csv')
x=df.iloc[:,1:-1].values
y=df.iloc[:,-1].values
plt.scatter(x,y)
x=x.reshape(-1,1)
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
for i in range(4):
    x[:,i]=lab.fit_transform(x[:,i])
    print(lab.classes_)
    
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy')
dtc.fit(x,y)
y_pred=dtc.predict([[2,1,0,1]])
print(y_pred)
    