def main():
    s = input()
    res = list()
    aberto = 0
    last = 0
    cont = 0
    for i in s:
        i = int(i)
        
        if cont == 0:
            for c in range(i):
                res.append('(')
                aberto += 1
            res.append(str(i))  
            for c in range(aberto):
                res.append(')')
                aberto -= 1
        else:
            if last > i:
                for c in range(i):
                    del res[-1]
                res.append(str(i))
                for c in range(i):
                    res.append(')')
                    aberto -= 1
            elif last < i:
                for c in range(last):
                    del res[-1]
                for c in range(abs(last-i)):
                    res.append('(')
                res.append(str(i))
                for c in range(i):
                    res.append(')')
            else:
                for c in range(i):
                    del res[-1]
                res.append(str(i))
                for c in range(i):
                    res.append(')')     
        last = i
        cont += 1 
    return ''.join(res)


t = int(input())
for i in range(t):
    print(f'Case #{i+1}: {main()}')
