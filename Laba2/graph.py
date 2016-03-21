import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
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
print(liney)
# print(lc)
# plt.title("T(a)")
# plt.plot(a,T,'.-r')
# plt.show()

T2a = [T[i]**2 * a[i]/100.0 for i in range(len(a))]
a2 = [x**2 / 10000.0 for x in a]
plt.plot(a2 ,T2a , 'o--g')
for i in range(len(a)):
    print (str(a2[i]) + " " + str(T2a[i]))


b = 0;
sx = 0
sy = 0
sx2 = 0
n = len(a2)
for i in a2:
    sx += i
    sx2 += i**2
xcp = sx / n

for i in T2a:
    sy += i
ycp = sy / n


smult = 0;
for i in range(n):
    smult += a2[i] * T2a[i]
k = (n * smult - sx * sy) / (n * sx2 - sx**2)
b = ycp - xcp * k
I2 = [b + k*x for x in a2]
plt.plot(a2, I2, '-r')
plt.grid(True , linewidth=0.3);
plt.title("k = " + str(k)  + " " + "b = " + str(b))
# plt.show()
print("lool")
#print(1 / k)
#print((1/k) * 4 * (3.14**2))
print (sqrt((b / k) * 12))
