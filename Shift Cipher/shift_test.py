#shiftTest.py
'''
Prepares a plaintext file for manipulation by encoding and decoding.

Tests a plaintext file against the encoding and decoding methods.
'''

#imports
from random import randint
from shift_cipher import *


#make text all lower-case and strip non-alpha chars
def prepare(filename):
    infile = open(filename,'r')
    text = infile.read()
    infile.close()
    text = text.lower()
    string = ''
    for char in text:
        if char.isalpha():
            string += char
    return string

#pulls the offset of a shifted text
def simpleShiftBreak(string):
    '''assumes the char with highest frequency corresponds to e'''
    #build an empty list
    freqLst = []
    for i in range(26):
        freqLst.append(0)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    #calculate frequency
    for i in string:
        freqLst[ord(i)-97] += 1
    mostFreq = max(freqLst)
    #associate most frequent to e and return value
    for idx,i in enumerate(freqLst):
        if (freqLst[idx] == mostFreq):
            return (ord(alpha[idx])-ord('e'))
        

#decodes 200 strings and returns the percent correct
def runTest(string,wordLen):
    count = 0
    correct = 0
    while(count<200):
        #build and break a new string
        shiftKey = randint(0,25)
        textStart = randint(0,(len(string)-wordLen))
        newStr = string[textStart:textStart+wordLen]
        shifted = shift(newStr,shiftKey)
        shiftValue = simpleShiftBreak(shifted)%26
        #check returned value against actual key
        if  shiftKey == shiftValue:
            correct +=1
        count+=1
    #return percentage
    return correct/200
    

#test the shiftCipherBreaker for strings of length a through b
def testsimple(a,b,filename='innocents.txt'):
    pt = prepare(filename)
    for i in range(a,b+1):
        percentCorrect = runTest(pt,i)
        print('{}: {}'.format(i,percentCorrect))

