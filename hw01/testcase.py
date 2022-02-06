def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n >= 1:
        print(n)
        count += 1
        if n > 1 and n % 2 == 0:
            n = n // 2
        elif n > 1 and n % 2 != 0:
            n = n * 3 + 1
        else:
            n = 1
            break

    return count 