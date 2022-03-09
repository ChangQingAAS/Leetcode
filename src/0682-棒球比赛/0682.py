res = []
    for item in ops:
        if item not in ['+', 'D', 'C']:
            res.append(int(item))

        if item == '+':
            tmp1 = res.pop()
            tmp2 = res.pop()
            res.append(tmp2)
            res.append(tmp1)
            res.append(tmp2 + tmp1)

        if item == 'D':
            tmp1 = res.pop()
            res.append(tmp1)
            res.append(tmp1 * 2)

        if item == 'C':
            res.pop()
    return sum(res)