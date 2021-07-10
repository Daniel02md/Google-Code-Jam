t = int(input())
for c in range(t):
    n = int(input())
    main = list()
    sec = list()
    for i in str(n):
        main.append(int(i))
        sec.append(0)
    for p, i in enumerate(main):
        if i == 4:
            main[p] = main[p] - 1
            sec[p] = sec[p] + 1
    result = [''.join(list(map(str, sec))), ''.join(list(map(str, main)))]
    print(f"Case #{c+1}: {' '.join(result)}") 