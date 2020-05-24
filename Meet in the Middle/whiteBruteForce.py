#whiteBruteForce.py
'''
initiates a brute force attack on a quarterDES that includes a one-time-pad
with a second key k2
'''

from quarterDES import impqtE, impqtD

#checks a list of offsets for equality, then returns true or false
def checkOffset(lst):
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            return False
    return True

#implements a brute force attack on a whitened quarterDES
def whiteBruteForce(lst):
    for i in range(2**16):
        offset = []
        for pair in lst:
            ct = impqtE(pair[0],i,0)
            offset.append(ct ^ pair[1])
        if checkOffset(offset) == True:
            print(i,offset[0])
            return (i,offset[0])

