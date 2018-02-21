#encoding:utf-8
#encoding:utf-8
import math


n = 9
i = 2
factors = []


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def generate_factors():
    for factor in factors:
        yield factor


while i * i <= n:
    while n % i == 0:
        n /= i
        if is_prime(i):
            factors.append(i)
    if n > 1:
        if is_prime(n):
            factors.append(n)
    i += 1


if __name__ == '__main__':
    generator = generate_factors()
    while True:
        choice = raw_input()
        if choice == 'n':
            break
        else:
            print generator.next()
