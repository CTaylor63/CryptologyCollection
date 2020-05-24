#sbox.py
'''
Implements an s-box to transform 6-bit integers into 4-bit output
'''

sbox4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
         [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
         [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
         [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]


#s4 converts an int to a binary and returns the corresponding int from sbox4
def s4(num):
    bnum = '{0:06b}'.format(num)
    if len(bnum)>6:
        raise ValueError('Number must be 6 bits or less in size')
    #print('bnum:',bnum)
    row,col = int(bnum[0]+bnum[-1],2),int(bnum[1:-1],2)
    #print('col: {}, row: {}'.format(col,row))
    return sbox4[row][col]


#calculates the numer of bits that differ in two numbers
def diff(num1,num2):
    bin1 = '{:04b}'.format(num1)
    bin2 = '{:04b}'.format(num2)
    if len(bin1) > 4 or len(bin2) > 4:
        raise ValueError('Arguments must be integers of 4 bits or less in size')
    numDiff = 0
    for idx, i in enumerate(bin1):
        if bin2[idx] != i:
            numDiff += 1
    return numDiff



def testBox():
    for i in range(64):
        count = 0
        while (count < 6):
            num = count
            bnum = '{:06b}'.format(i)
            #print('num: {}, bnum: {}'.format(num,bnum))
            pair = bnum
            #print('pair: ',pair)
            if pair[count] == '0':
                pair = pair[:count]+'1'+pair[count+1:]
            else:
                pair = pair[:count]+'0'+pair[count+1:]
            #print('newpair: ',pair)
            #print(int(bnum,2),int(pair,2))
            intpair = int(pair,2)
            difference = diff(s4(i),s4(intpair))
            if difference <= 1:
                return False
            print('x: {}, x\': {}, #diff: {}'.format(i,intpair,difference))
            count +=1
    print('All input differences fine')
