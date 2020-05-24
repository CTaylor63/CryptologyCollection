#LFSR.py - Linear Feedback Shift Register

from random import *


reg = {}

#Registers s_{n-1} ... s_0 are stored in list reg:
#
#   reg[n-1]   reg[n-2]   ... reg[0]
#   s_{n-1}  s_{n-2}       s_0
#
#when displaying reg, we need to reverse order, so reg[0] is rightmost

def seed_reg():
    global reg
    reg = seed[:] #create copy of seed

#implements s_{n+2} = s_{n+1} + s_{n}
def s():
    global n, reg
    new_bit = (reg[2] + reg[1] + reg[0]) % 2
    out_bit = reg[0]
    reg = reg[1:]
    reg.append(new_bit)
    return out_bit

def cur_reg():
    'display current state of register reg'
    return ''.join(map(str, reg[::-1])) #or use loop; displaying reg


f = s #or some other linear feedback shift register
seed = [1,0,0,0] #for s

seed_reg()

for i in range(20):
    print('Register: {}  Output: {}'.format(cur_reg(),f()))


