#bruteforce.py
'''
executes a brute force attack on the quarterDES encryption system
'''

from quarterDES import qtE

def bruteforce(lst):
    lstKeys = []
    finalLst = set()
    for i in lst:
        iKeys = []
        pt = i[0]
        ct = i[1]
        for key in range(2**16):
            val = qtE(pt,key)
            if val == ct:
                iKeys.append(key)
        lstKeys.append(iKeys)
    if len(lstKeys) == 1:
        return lstKeys
    for i in range(len(lstKeys)-1):
        #print(lstKeys[i],lstKeys[i+1])
        finalLst.update(set(lstKeys[i]) & set(lstKeys[i+1]))
    return finalLst
