import numpy as np
import matplotlib.pyplot as plt
from math import *

X = np.array([  5.37588  , 10.224963 , 15.147621 ,  19.70829  , 24.667245])
Y = np.array([  9801.  ,  16744.36  , 27822.24  , 29584.  ,  43890.25])
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

DY = [[ y - 129.4 , y + 129.4] for y in Y]

kr =  100
# plt.figure(figsize=(15,7))
# plt.grid(True)
# plt.title('$u^2(F)$')
# plt.xlabel(r'$F$,H')
# plt.ylabel(r'$u^2$ ,$ (m/s)^2$')
# # plt.scatter(X, Y, s=129.4 ,marker='+', color='g')
# plt.plot(X,OY,'--r')
# plt.plot(X,Y,'-b' , alpha=0.5)
# for i in range(len(Y)) :
#     plt.plot([X[i],X[i]], DY[i], color='g')
# plt.xlim([5,25])
# plt.ylim([7000,45000])
# plt.savefig('u2.png') 
# plt.show()

ro = 1 / k
sro = 1 / k**2 * sk
print(ro * 10 ** 3)
print(sro * 10 ** 3)
