import math

def pollard_strassen(n):
    """Pollard factorizing function"""
    if n <= 1:
        print("Number must be > 1")

        def g(x):
            return (x * x + 1) % n

        x, y, d = 2, 2, 1

        while d == 1:
            x, y, d = g(x), g(g(y)), math.gcd(abs(x - y), n)

        if d != 1:
            return d
        return None
