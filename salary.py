import numpy as np
import pandas as pd
df=pd.read_csv('sal.csv',names=['age','workclass','fnlwgt','education','education_name','marital_status','occupation','relationship','race','gender','capital_gain','capital_loss','house_per_week','native_country','salary'],na_values=' ?')
df.isnull().sum()
x=df.iloc[:,0:14].values
y=df.iloc[:,-1].values
temp=x[:,[1,6,13]]
temp=pd.DataFrame(temp)
temp[0].value_counts()
temp[0]=temp[0].fillna('Private')
temp[1].value_counts()
temp[1]=temp[1].fillna('Prof-speciality')
temp[2].value_counts()
temp[2]=temp[2].fillna('United-States')
temp.isnull().sum()
x[:,[1,6,13]]=temp
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
for i in [1,3,5,6,7,8,9,13]:
    x[:,i]=lab.fit_transform(x[:,i])
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('One',OneHotEncoder(categories='auto'),[1,3,5,6,7,8,9,13])],remainder='passthrough')
x=ct.fit_transform(x)
x=x.toarray()