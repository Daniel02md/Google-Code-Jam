def decrypter():
    n, none= tuple(map(int, input().split()))
    l = list(map(int, input().split()))
    
    prime = list()
    result = list()
    for i in range(3, n+1):
        test = 0
        for p in range(1, i+1):
            if i % p ==0:
                test += 1
        if test <= 2:
            prime.append(i)
    cond = False
    for i in prime:
        for j in prime:
            if i*j == int(l[0]):
                result.append(i)
                result.append(j)
                del l[0]
                cond = True
                break
        if cond:
            break

    while len(l) > 0:
        if len(l) == 0:
            break
        result.append(l[0]//result[-1])
        del l[0]
    lista = result[:]
    lista.sort()

    return lista, result


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for c in range(t):

    ord, main  = decrypter()
    ord = sorted(set(ord))
    res = str()
    for i in main:
        for p, l in enumerate(ord):
            if i == l:
                res += alpha[p]
                break
    print(f'Case #{c+1}: {res}')