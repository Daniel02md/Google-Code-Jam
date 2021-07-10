def main():
    n = int(input())
    matrix = list()
    arr = list()
    for v in range(n):
        arr.append(input().split())
    for item in arr:
        temp = list()
        for i in item:
            temp.append(int(i))
        matrix.append(temp[:])
        temp.clear()

    #trace
    trace = list()
    for i in range(len(matrix)):
        trace.append(matrix[i][i])
    trace = sum(trace)
    


    r = None
    rows = 0
    
    for item in matrix:
        for p, i in enumerate(item):
    
            if i in item[p+1:]:
                r = True
        if r:
            rows += 1
    c = None
    cols = 0
    for co in range(len(matrix)):
        temp_cols = list()
        for item in matrix:
            temp_cols.append(item[co])
        for p, i in enumerate(temp_cols):
            if i in temp_cols[p+1:]:
                c = True
        if c:
            cols += 1
        c = False
        temp_cols.clear()

    return ' '.join([str(trace), str(rows), str(cols)])
        

t = int(input())
for i in range(t):
    print(f'Case #{i+1}: {main()}')