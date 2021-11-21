def addition(n):
    return helper(n,0)


def helper(n,summ):
    if n // 10 == 0:
        return summ + n
    else:
        summ += (n % 10)
        n //= 10
        return helper(n,summ)

