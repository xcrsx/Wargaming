# Two functions are presented that determine the parity of an integer.
# The implementation of the solution to this problem by modulo division 
# looks more clear but is a slower solution. The solution using the bitwise
# operation '&' does not look so obvious, but more efficient due to the work
# with the bit representation of the number.


def isEven(value):
    return value % 2 == 0

def isEven_2(value):
    return value & 1 == 0