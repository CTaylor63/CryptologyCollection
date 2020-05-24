#pollard.py
'''
determines a factor of a large product of two primes n
'''

from fractions import gcd
from random import randrange

def pollard(n):
    a = randrange(n)
    if gcd(a,n) != 1:
        print("gcd(a,n) != 1, base: {}".format(a))
        return
    b = a
    for i in range(2,n):
        b = (b**i) % n
        divisor = gcd(b-1,n)
        if divisor != 1:
            print("i: {}, base: {}, prime factor: {}".format(i,a,divisor))
            return
    print("No match")


