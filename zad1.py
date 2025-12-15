n = 28
p = 1
q = n
licznik = 0
def alg(n, p = 1, q = n):
    global licznik
    while p < q:
        s = (p+q) // 2
        licznik += 1
        if s*s*s < n:
            p = s + 1
        else:
            q = s
    return p
#zad1.1
#print(alg(n), licznik)
#odp: 28 - 4, 64 - 4, 80 - 5

#zad1.2
'''for i in range(2000):
    print(i, alg(i))'''

#odp: min - 730, maks - 1000

#zad1.3
#odp: A
