#zad2.1
#sp.1
from math import inf
'''min_tg = inf
dane = [[1, 3], [3, 4], [2, 1], [-2, 2]]
min_xy = [0, 0]
for x, y in dane:
    if x / y < min_tg:
        min_tg = x / y
        min_xy = [x, y]
print(min_tg, min_xy)'''

#sp.2 - nie używając list itp.
X = [1, 3, 2, -2]
Y = [3, 4, 1, 2]
n = len(X)

'''x = X[0]
y = Y[0]

i = 0
while i < n:
    if X[i] / Y[i] < x / y:
        x, y = X[i], Y[i]
    i += 1

print(x, y)'''

#zad2.2
i, j = 0, 0
while i < n:
    j = 0
    while j < n - 1:
        if X[j] /Y[j] > X[j + 1] / Y[j + 1]:
            #X[j], X[j + 1] = X[j + 1], X[j]
            temp = X[j]
            X[j] = X[j + 1]
            X[j + 1] = temp
            temp = Y[j]
            Y[j] = Y[j + 1]
            Y[j + 1] = temp
        j = j + 1
    i = i + 1
for i in range(4):
    print(X[i], Y[i])
