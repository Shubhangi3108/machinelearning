import numpy as np
import time
st=time.time()
my_list=list(range(1000000))
for i in range(10):my_list2=2*my_list
et=time.time()
print("execute time for list:",et-st)
st=time.time()
my_arr=np.array(range(1000000))
for i in range(10):my_arr2=2*my_arr
et=time.time()
print("execute time for numpy:",et-st)