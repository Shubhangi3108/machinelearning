import numpy as np
from sklearn.datasets import load_breast_cancer
df=load_breast_cancer()
x=df.data
y=df.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(max_iter=10000)
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
y_pred

#confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
acc=(60+46)/(46+4+4+60)
print(acc)

from sklearn.metrics import accuracy_score,precision_score
print(accuracy_score(y_test,y_pred))
print(precision_score(y_test,y_pred))
