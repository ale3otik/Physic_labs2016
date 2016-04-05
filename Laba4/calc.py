from math import *
import numpy as np
M = 2.9
L = 2.255
g = 9.8067

m1 = [516 , 515 , 520 , 524 , 527 , 511 , 523 , 516]
x1 =  [15 , 17 , 16 , 14 , 15 , 14 ,14 , 15]
x = [0.001  * xi for xi in x1]
mn = [xi * 0.001 * 0.001 for xi in m1]
# print(x)
# print(mn)
u = [ M / mn[i] * sqrt(g/L) * x[i] for i in range(8)]
us = 0
us2 = 0
for ui in u :
    us += ui
    us2 += ui**2
# print(us/8)
print(sqrt((us2/8.0 - (us/8.0)**2)))

uss = 0
for ui in u :
    uss += (ui - us/8.0)**2
# print(sqrt(uss/8.0))
# print(sqrt(0.2**2 + 1.5**2))
sigmxi = sqrt(0.2**2 + 1.5**2) * 1e-3
# print(mn)
# print(x)
dl2 = [(0.5 * M / mn[i] * sqrt(L/g) * g / L**2 * x[i] * 0.005)**2 for i in range(8)]
dx2 = [(M/mn[i] * sqrt(g/L) * sigmxi) ** 2 for i in range(8)]
dm2 = [(M/mn[i]**2) * sqrt(g/L) * x[i] * (0.5) * 1e-6 for i in range(8)]

print(dm2)
print(dl2)
print(dx2)

sigmi = [sqrt(dx2[i] + dl2[i] + dm2[i]) for i in range(8)]

sx = ""
sl = ""
sm = ""
for i in range(8) :
    sx += "&" + str(round(dx2[i],1))
    sl += "&" + str(round(dl2[i],1))
    sm += "&" + str(round(dm2[i],1))

print(sx)
print(sl)
print(sm)


# print(ss)

# print(sigmi)
# sr = ""
# for ui in u:
    # sr += "&" + str(round(ui,0))
# print(u)
# print(sr)

# sm = 0
# mcp = 0;
# sm2 = 0
# sm2a = 0
# for k in m1 :
#     sm += (0.001) * k
#     mcp += k
#     sm2a += (0.001 * k) ** 2
# mcp = 0.001 * mcp/8.0
# for k in m1 :
#     sm2 += ((0.001 * k) - mcp)**2


# print(sqrt(sm2 / 8.0))
# # print(sm)
# m = [x * 0.001 for x in m1]
# print(np.sum(m))
# g = 9.8
# # L = 
# # u = 

# dx = [15,17,16,14,15,14,14,15]
# sx = ""
# for x in dx :
#     sx += "&" + str(x)
# print(sx)
# print(0.0005 * 8)

# # dxp = m / M * sqrt(L/g) * u

# # x = [15]