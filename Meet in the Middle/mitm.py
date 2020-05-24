#mitm.py
'''
implements a meet in the middle attack on quarterDES found in quarterDES.py
'''

from quarterDES import *

global keys

#build a table of possible ciphertexts associated with the plaintext
def buildtable(pair):
    pt = pair[0]
    global keys
    keys = {}
    for i in range(2**16):
        encrypted = qtE(pt,i)
        if encrypted not in keys:
            keys[encrypted] = [i]
        else:
            keys[encrypted] += [i]

#compares all possible decrypts to keys in the table keys        
def attack(pair):
    ct = pair[1]
    global keys
    keyPairs = []
    for i in range(2**16):
        decrypted = qtD(ct,i)
        try:
            if keys[decrypted]:
                keyPairs.append([i,keys[decrypted]])
        except KeyError:
            pass
    return keyPairs

#compares potential key pairs to the list of (pt,ct)
def compare(pairs,keylist):
    actual = keylist
    for i in pairs[1:]:
        for keyset in actual:
            newset = []
            for k1 in keyset[1]:
                if qtE(qtE(i[0],k1),keyset[0]) == i[1]:
                    newset.append(k1)
            keyset[1] = newset
        cleaned = []
        for i in actual:
            if i[1] != []:
                cleaned.append(i)
        actual = cleaned
    return actual

def mitm(lst):
    global keys
    potential = []
    buildtable(lst[0])
    potential = attack(lst[0])
    actual = compare(lst,potential)
    print(actual)

'''
from random import randrange
k1 = randrange(2**16)
k2 = randrange(2**16)
pt1 = 12345
pt2 = 6789
ct1 = qtE(qtE(pt1,k1),k2)
ct2 = qtE(qtE(pt2,k1),k2)
pair = (pt1,ct1)
pairs = [(pt1,ct1),(pt2,ct2)]
'''
