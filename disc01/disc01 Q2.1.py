def above_zero(i):
    "test if i is above 10"
    return i > 10


def is_even(i):
    "test if i is even number"
    return i % 2 == 0



def keep_ints(cond, n):
    "Print out all integers 1...i...n when cond(i) is true"
    i = 1
    while i < n:
        if cond(i) == True:
            print (i)
            i = i + 1
        else:
            i = i + 1 

