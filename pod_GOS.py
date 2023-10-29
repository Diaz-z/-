import random
from prvz import *
from hash import *
from math import gcd as bltin_gcd


def coprime2(one, two):
    return bltin_gcd(one, two) == 1


'''
b = random.getrandbits(768)
p = random.getrandbits(1024)
q = random.getrandbits(256)
while p != (b * q + 1):
    q = random.getrandbits(256)
    while not miller_rabin(q, 40):
    b = random.getrandbits(768)

p = b * q + 1
print(p, q)
a = random.randint(1, 1000000000)
while pow(a, q, p) != 1:
    a = random.randint(1, 1000000000)
'''

b = int(random.randint(1, 10))
print(f'b= {b}')
p = int(random.randint(1, 10000))
q = int(random.randint(1, 1000))
while p != (b * q + 1):
    p = int(random.randint(1, 10000))
    while not is_prime(p):
        p = int(random.randint(1, 1000))
    q = int(random.randint(1, 1000))
    while not is_prime(q):
        q = int(random.randint(1, 1000))
print(f'p,q= {p, q}')
g = int(random.randint(1, 1000))
el = ((p - 1) // q)
a = pow(g, el, p)
while a < 1:
    g = int(random.randint(1, 1000))
    a = pow(g, (p - 1 // q), p)
    print(f'a= {a}')

x = random.randint(1, q)
y = pow(a, x, p)
print('Введите сообщение: ')
m = input()
h = md5(m)
h = int(h, 16) % q
k = random.randint(1, q)
r = pow(a, k, p) % q
s = ((k * h) + (x * r)) % q
while r == 0 or s == 0:
    k = int(random.randint(1, q))
    r = pow(a, k, p) % q
    s = ((k * h) + (x * r)) % q
print(f'Число: {m} Подпись: {r, s}')
range_ = range(0, q)
if (r > 0) and (q > r) and (s > 0) and (q > s):
    u1 = ((pow(h, -1, q)) * s) % q
    u2 = (-r * pow(h, -1, q)) % q
    v = ((pow(a, u1, p) * pow(y, u2, p)) % p) % q
    print(v, ' = ', r)
    if v == r:
        print('Проверка пройдена')
