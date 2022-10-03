cache = {}

def sole(m, n, t):
    if (m, n, t) in cache:
        return cache[(m, n, t)]
    else:
        cache[(m, n, t)] = m*n*t
        return m*n*t

list0 = []
for i in range(4):
    list0.append((1, 2, 3))
    list0.append((4, 5, 6))
for i, j, k in list0:
    print(sole(i, j, k))
