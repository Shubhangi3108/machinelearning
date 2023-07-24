import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('blood.xlsx')
x=df.iloc[:,1].values
y=df.iloc[:,2].values
'y=df.iloc[:,-1].values (this can also be used)'
plt.scatter(x,y)
x=x.reshape(-1,1)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#all x and y consider as train data
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x,y)
y_pred=lin_reg.predict([[39]])
y_pred

#y=mx+c
m=lin_reg.coef_
c=lin_reg.intercept_
y_pred1=m*39+c
y_pred1