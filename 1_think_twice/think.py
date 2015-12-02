#!/usr/bin/env python
'''
Problem:
Given an unreadable string and three hints, decode the message.
1. K --> M
2. O --> Q
3. E --> G

Solution:
This is Ceasar's cypher.

The solution suggests using string.maketrans().  This works, but it
requires a translation table.

It also seems to have issues in Python 3 string.maketrans was deprecated
and then removed.  Strings are not bytes. They are Unicode.

I had considered using a dictionary for the table, but felt it makes
reusability much harder if the mapping K--> M changed to something
else like K --> P.  A new table is required.

One could write a function to generate the translation table.  This would be
quite useful if the input strings were VERY large. At least I think so. This
could be profiled. shift_ord() is almost doing this.
'''

import string

def shift_ord(cha, shift_n):
    '''
    Shift a character in the range [a-z] or [A-Z] N places wrapping as required.
    Shifts may be positive or negative.
    '''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    cha_shifted = cha  # If not in lower, nor in upper, then no shift

    if cha in lower:
        idx = lower.find(cha)
        if shift_n < 0:  # Handle wrapping before a
            while idx - shift_n < 0:
                idx += 26
        cha_shifted = lower[(idx + shift_n) % 26]  # Use % for wrapping past z
    elif cha in upper:
        idx = upper.find(cha)
        if shift_n < 0:  # Handle wrapping before A
            while idx - shift_n < 0:
                idx += 26
        cha_shifted = upper[(idx + shift_n) % 26]  # Use % for wrapping past Z
    return cha_shifted

def explore(msg, shift):
    '''Find a solution.'''
    msg_shifted = ''.join([shift_ord(cha, shift) for cha in msg])

    print '\nEncrypted message:'
    print msg_orig
    print '\nDecrypted message:'
    print msg_shifted

if __name__ == '__main__':
    msg_orig = \
        "g fmnc wms bgblr rpylqjyrc gr zw fylb. " + \
        "rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr" + \
        "ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    explore(msg_orig, 2)
