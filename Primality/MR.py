#MR.py - Miller Rabin primality test

from random import randint

def expm(a,x,n):
    '''returns a**x mod n calculated via repated squaring'''
    if x < 0:
        return
    else:
        product = 1
        power = a
        while x > 0:
            if x % 2 == 1:
                product = (product * power ) % n
            power = (power*power) % n
            x = x//2
        return product

#run Miller/Rabin primality test for a single base a
def simpleMR(n):
    'Miller/Rabin for single base'
    r = n-1
    u = 0
    while r % 2 == 0:
        r = r//2
        u += 1
    #return (u,r)
    a = randint(2, n-1)
    b = expm(a,r, n)
    if b != 1 and b != n-1:
        for j in range(0,u): #wrong in book, need u iterations
            b = (b*b) % n
            #print(b)
            if b == 1:
                print('{} is composite'.format(n))
                return False
            if b == n-1: #case missing in book
                b = 1
                break
        if b != 1:
            print('{} is composite'.format(n))
            return False
    print('{} is probably prime'.format(n))
    return True

def MR(n):
    'Miller/Rabin primality test for 100 bases'
    r = n-1
    u = 0
    while r % 2 == 0:
        r = r//2
        u += 1
    #test 100 random bases
    for i in range(100):
        a = randint(2, n-1)
        b = expm(a,r, n)
        for j in range(0,u): #wrong in book: need u iterations
            if b == 1 or b == n-1:
                b = 1
                break #n is probably prime
                #break out of for #loop to test next a, need b = 1
                #so as not to trigger b!=1 test below
                #the p-1 case is missing in book
            b = (b*b) % n
            if b == 1:
                return False #n is composite by Fermat's Principle
        if b != 1:
            return False #n is composite by Fermtat's Little Theorem
    return True #n is probably prime

def nextprime(n):
    s = n
    ct = 1
    while not(MR(s)):
        s = s+1
        ct += 1
        #print(ct)
    return s
