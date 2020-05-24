#steps.py
'''
tests the number of steps from a random number of x binary length to the next prime
'''

from MR import nextprime
from random import randrange

def steps(num):
    stepLst = []
    for i in range(100):
        randNum = randrange(2**(num-1),2**(num))
        prime = nextprime(randNum)
        stepLst.append(prime-randNum)
    avg = sum(stepLst)/len(stepLst)
    print("{} avg attempts at length {}".format(avg,num))
