#shiftCipher.py
'''
Encodes and decodes a plaintext string
'''

#turn text into list of numbers (ASCII values)
def encode(text):
    lst = [(ord(letter) - ord('a')) for letter in text]
    return lst

#turn list of ASCII values into text
def decode(lst):
    text = ''.join([chr(ord('a')+code) for code in lst])
    return text

#shift each letter code by 26, and take result mod 26
def shift(pt,k):
    'plaintext pt, shift k'
    ptlst = encode(pt)
    ctlst = [(x+k) % 26 for x in ptlst]
    return decode(ctlst)
