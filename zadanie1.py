#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


c1 = '''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


c2 = '''
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


c3 = '''
def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product
'''


c4 = '''
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
'''


c5 = '''
from functools import lru_cache
@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''


c6 = '''
from functools import lru_cache
@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
'''


if __name__ == '__main__':
    print('Результат рекурсивного факториала:', timeit.timeit(setup=c1, number=1000))
    print('Результат рекурсивного числа Фибоначи:', timeit.timeit(setup=c2, number=1000))
    print('Результат итеративного факториала:', timeit.timeit(setup=c3, number=1000))
    print('Результат итеративного числа Фибоначи:', timeit.timeit(setup=c4, number=1000))
    print('Результат факториала с декоратором:', timeit.timeit(setup=c5, number=1000))
    print('Результат числа Фибоначи с декоратором:', timeit.timeit(setup=c6, number=1000))