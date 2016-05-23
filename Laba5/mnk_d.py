import numpy as np
import matplotlib.pyplot as plt
from math import *

X = np.array([0,1,2,3,4])
Y = np.array([0 , 208.7, 418.3 , 629.0 , 837.1])
th = np.polyfit(X,Y,1)
k = th[0]
b = th[1]

print(k)
print(b)

sk = 1/(len(X)**0.5) * ((np.mean(Y**2) -  np.mean(Y)**2)/(np.mean(X**2) -  np.mean(X)**2) - k**2) **0.5
sb = sk * ((np.mean(X**2) -  np.mean(X)**2))**0.5
print(sk)
print(sb)

OY = [k * x + b for x in X]


kr =  100
plt.figure(figsize=(15,7))
plt.grid(True)
# plt.scatter(X, Y, s=100 ,marker='+', color='g')
plt.plot(X,OY,'--r')
plt.plot(X,Y,'-ob' , alpha=0.5)
# plt.xlim([-0.1,len(X)-1 + 0.1])
# plt.ylim([-10,Y[len(X)-1] + 100])
plt.savefig('m4.png') 
plt.show()