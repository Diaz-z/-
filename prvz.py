import random

def gcd(n, m):
    if m == 0:
        return 0
    else:
        return gcd(m, n % m)


def task(n, m):
    return gcd(n, m) == 1


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def is_prime1(num):
    if num <= 1:
        return False
    b = num ** 0.5
    i = 2
    while i <= b:
        if num % i == 0:
            return False
        print(i)
        i = i + 1
    return True


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def Prime(n):
    nd = 2
    if n & 1 == 0:
        nd = 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            nd = d
        d = d + 2
    if nd == 1:
        return True
    return False


def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n==3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True