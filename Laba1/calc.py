
# from math import *

# m =  (0.448 + 0.58)

# I = 0.085 * 0.085 * 0.58 / 2 + 0.1146 * 0.1146 * 0.448 / 2;
# r = 0.03
R = 0.1146
M = 0.4482
# dM = 0.0003
# z = 2.14
# dr = 0.0005
# dR = 0.0003
# dz = 0.01
# T = sqrt(I/k * m)
# print(T)
# print(k)
# dk = 9.8/(4 * 3.14 * 3.14) * sqrt(((r*dR/z)** 2) + ((R * dr / z) ** 2) + ((R * r * dz)/(z**2))**2);
k = (9.8 * 0.1146 * 0.03) / (4 * 3.14 * 3.14 * 2.14)
I0 = R**2 * M / 2


# # t = 3.834
# # m = 0.4482 + 0.5801 + 0.9752
# # r1 = 0.084
# # m1 = 0.9752

# # print r1**2 * m1

# # print ((0.21**2) * 0.7065)/12
# # print(0.21 * 0.0005 * 0.7065/6)
# # print k * m * (t**2) - I0
# # print k * sqrt((dM * t**2)**2 + (m * 2 * t * t * 0.005)**2)

# # print(6.58 + 9.836)
# # print R**2 * M / 2
# # print R * M * dM
# # print dk
# # print(79.027 / 19)
# # print(0.9/2, 2.75/2 ,  5.7 / 2 ,  6.7/2 ,  8.7 ,  10.7 , 14.7/2)
# # x = [50.532,50.686,52.048,55.297,57.383,61.748,66.124,76.614]
# # for i in range(8):
# #     print(x[i]/19)


from pylab import *
import random
import matplotlib.pyplot as plt

K = [0, 0.9/2, 2.75/2 ,  5.7 / 2 ,  6.7/2 ,  8.7/2 ,  10.7/2 , 14.7/2]
X = [(i/100)**2 for i in K]
# # print(X)
t = [50.532,50.686,52.048,55.297,57.383,61.748,66.124,76.614]
# # print((t[0]/19)**2 * k * ((2*0.5664 + 0.4482))
T = [i/19 for i in t]
I = [(tc**2) * k * (2*0.5664 + 0.4482) - I0 for tc in T]

b = 0;
sx = 0
sy = 0
sx2 = 0
for i in X:
    sx += i
    sx2 += i**2
xcp = sx / 8

for i in I:
    sy += i
ycp = sy / 8

smult = 0;
n = 8
for i in range(8):
    smult += X[i] * I[i]
b = (n * smult - sx * sy) / (n * sx2 - sx**2)
a = ycp - xcp * b
I2 = [a + b*x for x in X]
print("k = " + str(b))

# rx = ""
# ry = ""
dI = 0
dK = 0;
# for i in range(len(X)) :
    # dI = max(dI , abs(a + b*X[i] - I[i]));
    # if X[i] == 0 :
        # continue;

    # dK = abs((a + b*X[i])/ X[i] - I[i]/X[i]);
    # rx += ' & ' + str(round(X[i] , 7))
    # ry += ' & ' + str(round(I[i] , 5))
# print(dI)
# print(dK)
# print(rx)
# print(ry)

Imax = ((0.088)**2 * (0.5664 + 0.5653)) / (8.0);
Imin = ((0.078)**2 * (0.5664 + 0.5653)) / (8.0);
print( (Imax + Imin) / 2.0 )
print((Imax - Imin) / 2.0 )
print (0.5664 + 0.5653)

# plt.xlabel("$h^2 , [m^2]$", size=14)
# plt.ylabel('$I(h^2) , [kg * m^2]$', size=14)
# plt.plot(X, I, '-g', linestyle='--' , marker='o')
# plt.plot(X, I2, '-r')
# plt.grid(True , linewidth=0.3,);
# # plot(K, N, '-r')
# plt.show()

# print((0.00409896 - 0.00154) / 0.00242)