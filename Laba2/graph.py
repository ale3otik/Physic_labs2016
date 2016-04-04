import numpy as np
import matplotlib.pyplot as plt
from math import *
a = np.arange(4, 52, 4)
tlool = [53.87 , 43.19 , 36.68 , 33.28 , 31.69 , 30.90 , 30.57 , 30.68 , 31.13 , 31.31 , 31.85 , 32.69]
T = [x / 20 for x in tlool]
# linex = ""
liney = ""
# lc = "|c|"
for i in range(len(T)):
#     linex += '& ' + str(a[i]);
    liney += '& ' + str(round(T[i] , 3));
#     lc += "c|"

# print(linex)
# print(liney)
# print(lc)
# plt.title("T(a)")
# plt.plot(a,T,'.-r')
# plt.show()

T2a = [(T[i]**2 * a[i])/100.0 for i in range(len(a))]
a2 = [x**2 / 10000.0 for x in a]
plt.plot(a2 ,T2a , 'o--g')
# lineT2a = "$T^2 a , [c^2 m] $"
# linea2 = "$a^2 , [m^2]$"

# for i in range(len(a)):
#     lineT2a += " & " + str(round(T2a[i],3))
#     linea2 += " & " + str(round(a2[i],3))
#     # print (str(a2[i]) + " " + str(T2a[i]))
# print(linea2)
# print(lineT2a)

b = 0;
sx = 0
sy = 0
sy2 = 0
sx2 = 0
n = len(a2)
for i in a2:
    sx += i
    sx2 += i**2
xcp = sx / n
xcp2 = sx2/n

for y in T2a:
    sy += y
    sy2 += y**2
ycp = sy / n
ycp2 =  sy2 / n


smult = 0;
for i in range(n):
    smult += a2[i] * T2a[i]
k = (n * smult - sx * sy) / (n * sx2 - sx**2)
b = ycp - xcp * k
X = [0 , a2[len(a2) - 1]]
I2 = [b + k*x for x in X]
plt.plot(X, I2, '-r')
plt.grid(True , linewidth=0.3);
plt.title("k = " + str(k)  + " " + "b = " + str(b))
# plt.show()
print("lool")
# print(k);
# print(b);
#print(1 / k)
#print((1/k) * 4 * (3.14**2))
print (sqrt((b / k) * 12))
sigmk = 1 / sqrt(n) * sqrt((ycp2 - ycp**2) / (xcp2 - xcp**2) - k**2)
sigmb = sigmk * sqrt(xcp2 - xcp**2)

print("__")
print(sigmk)
print(sigmb)

print("__")
print(4 * pi**2 * 0.0037)
print(0.5 * sqrt(k / (12 * b)) * (12 * k * sigmb + 12 * b * sigmk) / (k**2))

print("__")
print(0.21 + 1 / (0.21 * 12 ))

