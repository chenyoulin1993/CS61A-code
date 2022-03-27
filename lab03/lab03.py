""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"

    def counting(a,b,smaller):
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        else:
            return counting(a, b, smaller-1)

    if a > b:
        smaller = b
        return counting(a,b,smaller)
    if a < b:
        smaller = a
        return counting(a,b,smaller)
    if a == b:
        return a 


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    step_count = 0
    def count(n, step_count):
        step_count+=1
        print (n)
        if n == 1:
            return step_count
        if n % 2 == 0:
            return count( n//2, step_count )
        else:
            return count(n*3+1,step_count )
    return count(n, step_count)
