#zad2.1
from math import inf
min_tg = inf
dane = [[1, 3], [3, 4], [2, 1], [-2, 2]]
min_xy = [0, 0]
for x, y in dane:
    if x / y < min_tg:
        min_tg = x / y
        min_xy = [x, y]
print(min_tg, min_xy)
