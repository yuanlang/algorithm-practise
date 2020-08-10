price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cut_rob_recursive(p, n):
    if n == 0:
        return 0
    q = -0x7fffffff
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rob_recursive(p, n - i))
    return q

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = -0x7fffffff
    if n == 0:
        q = 0
    else:
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

def memoized_cut_rod(p, n):
    r = []
    for _ in range(n + 1):
        r.append(-0x7fffffff)
    return memoized_cut_rod_aux(p, n, r)

def bottom_up_cut_rod(p, n):
    r = []
    for i in range(0, n + 1):
        r.append(0)
    r[0] = 0
    for j in range(1, n + 1):
        q = -0x7fffffff
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

length = (int)(input())
value = bottom_up_cut_rod(price, length)
print(value)
