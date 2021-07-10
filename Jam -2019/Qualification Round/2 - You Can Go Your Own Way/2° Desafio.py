def main():
    n = int(input())
    s =  list(i.upper() for i in input())
    for p, i in enumerate(s):
        if i == 'S':
            s[p] = 'E'
        else:
            s[p] = 'S'
    return ''.join(s)

t = int(input())

for i in range(t):

    print(f'Case #{i+1}: {main()}')