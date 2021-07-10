def main():
    n = int(input())
    principal = [list(map(int, input().split()))for c in range(n)]
    lista =  [principal[i][0] for i in range(len(principal))]
    fim = [principal[i][1] for i in range(len(principal))]
    limite = 1440
    cont = 0
    result = list()
    task = list()
    for p, num in enumerate(lista):
        
        if cont == 0:
            result.append(num)
            task.append([num, fim[p]])
            
        elif num > result[-1]:
            task.append([num, fim[p]])
            result.append(num)

        else:
            Lista = []
            for item in result:
                if item <= num:
                    Lista.append(item)
            
            if Lista == []:
                result.insert(0,num)
                task.insert(0,[num, fim[p]])
            elif max(Lista) in result:
                rep = []

                for posi,c in enumerate(result):
                    
                    if max(Lista) == c: 
                        
                        rep.append(c)
                        rep.append(posi)

                if len(rep) > 1:
                    result.insert(rep[-1]+1, num)
                    task.insert(rep[-1]+1, [num, fim[p]])


        cont += 1
    return task
t = int(input())
for count in range(t):
        
    maina = main()[:]
    print(maina)

    last = cond = None
    resp = princ = str()
    c = list()
    j = list()
    pode_c = pode_j = None
    for i in range(len(maina)):
        if i == 0: 
            princ = 'J'
            last = maina[i][1]
            resp += princ
            j.append(maina[i][1])
            pode_j = True
            continue

        if maina[i][0]-last >= 0:
            cond = True
            if princ == 'C':
                c.append(maina[i][1])
            if princ == 'J':
                j.append(str(maina[i][1]))
        else:
            cond = False

        if not cond:
            if princ == 'J':
                if i == 1:
                    princ = 'C'
                    c.append(maina[i][1])

                elif maina[i][0] - c[-1] >= 0:
                    c.append(maina[i][1])
                    
                else:
                    pode_c = False

            elif princ == 'C':
                if maina[i][0] - j[-1] >= 0:
                    j.append(maina[i][1])
                    princ = 'J'
                else:
                    pode_j = False
        
        if not pode_j and not pode_c:
            resp = 'IMPOSSIBLE'
            break
        resp += princ
        print(resp)
        last = maina[i][1]
    print(f'Case # {count+1}: {resp}')