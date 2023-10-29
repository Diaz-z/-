import random
from prvz import *
from hash import *
from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


p = int(random.randint(1, 1000000000))
while not is_prime(p):
    p = int(random.randint(1, 1000000000))
q = int(random.randint(1, 1000000000))
while not is_prime(q):
    q = int(random.randint(1, 1000000000))
g = gcd_extended(p, q)[1]
x = int(random.randint(1, p - 1))
y = pow(g, x, p)
print(f'Введите сообщение: ')
m = input()
h = md5(m)
h = int(h, 16) % p
print(f'Хэш: {h}')
k = int(random.randint(1, p - 1))
while not coprime2(k, (p - 1)):
    k = int(random.randint(1, p - 1))
r = pow(g, k, p)
u = (h - (x * r)) % (p - 1)
s = (pow(k, -1, (p - 1)) * u) % (p - 1)
pod = [m, r, s]
print(f'Сообщение с подписью: {pod}')
pr1 = (pow(y, r, p) * pow(r, s, p)) % p
pr2 = pow(g, h, p)
print(pr1, ' = ', pr2)
if pr1 == pr2:
    print('Проверка пройдена')
