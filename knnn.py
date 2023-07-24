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

#1 catagories wise
plt.scatter(x[y==0,0],x[y==0,1],label='Setosa')

plt.scatter(x[y==1,0],x[y==1,1],label='Versicolor')

plt.scatter(x[y==2,0],x[y==2,1],label='Verginica')
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.legend()
plt.title("Analysis of Iris Flower")

#2 catagories wise
plt.scatter(x[y==0,2],x[y==0,3],label='Setosa')

plt.scatter(x[y==1,2],x[y==1,3],label='Versicolor')

plt.scatter(x[y==2,2],x[y==2,3],label='Verginica')
plt.xlabel("patel length")
plt.ylabel("patel width")
plt.legend()
plt.title("Analysis of Iris Flower")

#3 catagories wise
plt.scatter(x[y==0,0],x[y==0,3],label='Setosa')

plt.scatter(x[y==1,0],x[y==1,3],label='Versicolor')

plt.scatter(x[y==2,0],x[y==2,3],label='Verginica')
plt.xlabel("Sapel length")
plt.ylabel("Patel width")
plt.legend()
plt.title("Analysis of Iris Flower")

#4 catagories wise
plt.scatter(x[y==0,2],x[y==0,1],label='Setosa')

plt.scatter(x[y==1,2],x[y==1,1],label='Versicolor')

plt.scatter(x[y==2,2],x[y==2,1],label='Verginica')
plt.xlabel("patel length")
plt.ylabel("sapel width")
plt.legend()
plt.title("Analysis of Iris Flower")

#5 catagories wise
plt.scatter(x[y==0,1],x[y==0,2],label='Setosa')

plt.scatter(x[y==1,1],x[y==1,2],label='Versicolor')

plt.scatter(x[y==2,1],x[y==2,2],label='Verginica')
plt.xlabel("sapel width")
plt.ylabel("patel length")
plt.legend()
plt.title("Analysis of Iris Flower")

#6 catagories wise
plt.scatter(x[y==0,3],x[y==0,0],label='Setosa')

plt.scatter(x[y==1,3],x[y==1,0],label='Versicolor')

plt.scatter(x[y==2,3],x[y==2,0],label='Verginica')
plt.xlabel("patel width")
plt.ylabel("sapel length")
plt.legend()
plt.title("Analysis of Iris Flower")