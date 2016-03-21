from math import *
# x = [31.43 , 31.72, 31.56 , 31.62 , 31.49 , 31.53]
x = [31.56 , 31.34 , 31.6 , 31.62 , 31.63 , 31.54]
ln = ""
# for v in x:
#     ln += "&" + str(v)
# print(ln)

s = 0
for i in x:
    s = s + i
Tcp = s/ (6 * 20)
tcp = s / 6;
xp = [p - tcp for p in x]


sigm = 0
for p in xp:
    sigm += p**2
sigm = sqrt(sigm / 5)

print(tcp)
print(Tcp)
print (sigm)
eps = sigm / (20 * Tcp)
print(eps)
# # print(sigm / (0.005 * Tcp))
# # print(10/7.5)
# print((5 * 60 + 30) / Tcp)


# print(31.40  / 20)
# Q = (pi * 330) / (Tcp * log(1.3))
# print(Q)
