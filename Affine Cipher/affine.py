#affine.py
'''
encodes and decodes using the affine cipher
'''

from random import *

freqE = [.0804, .0154,.0306,.0399,.1251,.023,.0196,.0549,
         .0726, .0016, .0067,.0414,.0253,.0709,.076,.020,
         .0011,.0612, .0654,.0925,.0271,.0099,.0192,.0019,
         .0173,.0009]

def encode(text):
    text = text.lower()
    
    lst = [(ord(letter) - ord('a')) for letter in text if letter.isalpha()]
    return lst

def decode(lst):
    text = ''.join([chr(ord('a')+code) for code in lst])
    return text

#affine cipher

def affine_h(pt,a,b):
    #helper function: works on coded text
    return [(a*x+b)%26 for x in pt]

def affine(pt,a,b):
    pt = encode(pt)
    return decode(affine_h(pt,a,b))

