# recursive approaches cannot handle larger inputs and will run into maximum
# recursion depth errors; iterative approaches are best for calculating
# the factorial for larger numbers


def factorial(x):
    y = 1
    for i in range(1, (x + 1)):
        y *= i
    return y

if __name__ == '__main__':
    import math
    for n in range(101):
        m = factorial(n)
        print n, ": ", m
        assert m == math.factorial(n)
