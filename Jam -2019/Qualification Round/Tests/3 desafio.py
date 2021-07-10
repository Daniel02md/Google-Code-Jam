def first(a, b):
    c = a
    while True:
        if b == 0:
            break
        a, b = b, a%b
    return a
def decrypter():
    n, l = map(int, input().split())
    lista = list(map(int, input().split()))
    e = list()
    temp = first(lista[0], lista[1])
    e.append(temp)
    e.insert(0, lista[0]//temp)
    del lista[0]

    for i in range(l):
        if len(lista) == 0:
            break
        e.append(lista[0]//e[-1])
        del lista[0]
    ecryp = sorted(set(e[:]))
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dec = dict()
    res = str()
    for p, i in enumerate(ecryp):
        dec[i] = alpha[p]
    for i in e:
        res += dec[i]
    
    return res
    
T = int(input())
for c in range(T):
    print(f'Case #{c+1}: {decrypter()}')