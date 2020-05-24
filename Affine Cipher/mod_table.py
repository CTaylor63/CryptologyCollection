#modTable.py
'''
prints a multiplication table for values mod num
'''

def printmod(num):
    print('  0 1 2 3 4 5 6 7 8 9')
    for i in range(0,num):
            lst = [0]*num
            for j in range(0,num):
                    lst[j] = (i*j)%num
            print(i,end=' ')
            for x in lst:
                    print(x,end=' ')
            print("")
    return

