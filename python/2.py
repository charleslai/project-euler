def fibonacci_sum(limit = 4000000):
    s = 0
    n0 = 1
    n1 = 1
    odd = True
    while n0 < limit and n1 < limit:
        # Odd index fibonacci case
        if odd:
            n0 = n0 + n1
            # update sum
            if n0 % 2 == 0:
                s += n0
        # Even index fibonacci case
        else:
            n1 = n0 + n1
            # update sum if new number is even
            if n1 % 2 == 0:
                s += n1
        # Update idx flag
        odd = not odd
    return s

print fibonacci_sum()



