t = int(input())

def main():
    trash = input()
    l = list(int(i) for i in input().split())
    def reverse(a, b, lista):
        posi_a = lista.index(a)
        posi_b = lista.index(b)
        L = lista
        L[posi_a] = (b-a) + a 
        L[posi_b] = (a-b) + b
    
        return(L)
        
    
    cost = 0
    for i in range(1, len(l)):
    
        j = l.index(min(l[i - 1 : len(l)]))
        cost += (j+1) - i + 1

        
        l = reverse(l[i-1], l[j], l)
        if l == sorted(l):
            return cost
        print(i, j, l)
        
    return cost
        

for i in range(t):
    print(f'Case #{i+1}: {main()}')
        
        