#expm.py
'''
repeated squaring
'''


def expm(a,x,n):
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
