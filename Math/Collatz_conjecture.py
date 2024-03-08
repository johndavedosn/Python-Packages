def is_odd(n) :
    return n % 2 != 0
def problem(n, r):
    memo = []
    memo.append(n)
    for _ in range(r) :
        rule = memo[-1] * 3 + 1 if is_odd(memo[-1]) else memo[-1] / 2
        memo.append(rule)
    return memo

for i in range(1, 30, 1):
    p_i = problem(i, 20)
    print("number : {} \n p : {}".format(i, p_i))

