#!/usr/bin/env python

'''
Find lower case characters surrounded by exactly three upper case
characters on each side.
'''

import pprint
import re

def is_big(cha):
    '''Is cha an upper case letter?'''
    ord_A = ord('A')
    ord_Z = ord('Z')
    ord_ch = ord(cha)
    if ord_ch >= ord_A and ord_ch <= ord_Z:
        return True
    return False

def is_small(cha):
    '''Is cha a lower case letter?'''
    ord_a = ord('a')
    ord_z = ord('z')
    ord_ch = ord(cha)
    if ord_ch >= ord_a and ord_ch <= ord_z:
        return True
    return False

def file_to_string():
    '''Read the file into a string.'''
    strg = ''
    with open('equality.txt', 'r') as infile:
        for line in infile:
            for cha in line:
                if cha != '\n':
                    strg += cha
    return strg

def explore():
    '''Find the solution'''
    strg = file_to_string()
    matches = re.findall('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', strg)
    pprint.pprint(''.join(matches))

if __name__ == '__main__':
    explore()

