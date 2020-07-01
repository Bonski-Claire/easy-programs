a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def least_difference(a, b, c):
    """
    Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
least_diff1 = least_difference(a, 10, 100)
least_diff2 = least_difference(b, 10, 100)
least_diff3 = least_difference(c, 10, 100)
print('diff1 = ', least_diff1)
print('diff2 = ', least_diff2)
print('diff3 = ', least_diff3)
print('diff4 = ', min(least_diff1, least_diff2, least_diff3))
help(least_difference)