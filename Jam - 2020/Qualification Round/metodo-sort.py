fim = [4, 10, 9, 6, 8, 12]
lista = [2, 9, 8, 5, 7, 10]
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
print(task)
