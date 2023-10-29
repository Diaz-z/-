import random
from prvz import *
from hash import *
from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


p = int(random.randint(1, 1000000000))
while not is_prime(p):
    p = int(random.randint(0, 1000000000))
q = int(random.randint(1, 1000000000))
while not is_prime(q):
    q = int(random.randint(0, 1000000000))
N = p * q
f = (p - 1) * (q - 1)
d = int(random.randint(1, 1000000000))
while not coprime2(d, f):
    d = int(random.randint(1, 1000000000))
c = pow(d, -1, f)
print(f'Введите сообщение: ')
m = input()
y = md5(m)
y = int(y, 16) % p
s = pow(y, c, N)
print(f'Число: {m} подпись: {s}')
w = pow(s, d, N)
print(w, ' = ', y)
if w == y:
    print('Проверка пройдена')
