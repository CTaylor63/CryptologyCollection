#passwords.py
'''
implements an attack on a series of name, salt, hashed salted password pairs
'''

from expm import expm
from modinv import inv

D = {1, 12, 123, 12345, 123456, 1234567, 12345678, 123456789,
87654321, 87654321, 7654321, 654321,54321,4321,321, 21, 
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 33, 44, 55, 66, 77, 88, 99,
100,101, 1001, 10001, 100001,121,12321,1234321,123454321}

#executes a dictionary attack on the bad password implementation
#e is a value between 0 and 1
#n is any number
def passwordAttack(e,n):
    N = buildPassTable(e,n)
    for weakPass in D:
        ePass = expm(weakPass,e,n)
        if ePass in N.keys():
            print("Match! Name: {}, Password: {}".format(N[ePass][0],weakPass))

#builds a table of key value pairs to be compared to the weak passwords
#e is a value between 0 and 1
#n is any number
def buildPassTable(e,n):
    infile = open('passwords.txt')
    records = infile.readlines()
    infile.close()

    N = {}
    for record in records:
        record = record[1:-2] #remove ( and )
        (name, salt, spwd) = record.split(',')
        salt,spwd = eval(salt),eval(spwd)
        eSalt = expm(salt,e,n)
        invSalt = inv(eSalt,n)
        key = (spwd*invSalt)%n
        N[key] = (name,salt)
    return N
