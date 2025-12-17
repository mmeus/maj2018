dane = [w.strip() for w in open('sygnaly.txt')]
#zad4.1
'''for i in range(39, len(dane), 40):
    print(dane[i][9], end = '')'''
#print(''.join([[w.strip() for w in open('sygnaly.txt')][i][9] for i in range(39, len([w.strip() for w in open('sygnaly.txt')]), 40)]))

#zad4.2

#1. Tablica częstości:
'''max_s = ''
max_ile_roznych = 0

for s in dane:
    TC = [0] * 256
    for z in s:
        kod = ord(z)
        TC[kod] = 1
    ile_roznych = sum(TC)
    if ile_roznych > max_ile_roznych:
        max_ile_roznych = ile_roznych
        max_s = s
print(max_s, max_ile_roznych)'''

#zad4.3
'''czy = True
for s in dane:
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) > 10:
            czy = False
    if czy:
        print(s)
    czy = True'''