#!/usr/bin/env python
'''
Problem:
Given an unreadable string and three hints, decode the message.
1. K --> M
2. O --> Q
3. E --> G

Solution:
The solution suggests using string.maketrans().  This works, but it
requires a translation table.

It also seems to have issues in Python 3 string.maketrans was deprecated and then
removed.  Strings are not bytes. They are Unicode.

I had considered using a dictionary for the table, but felt it makes
reusability much harder if the mapping K--> M changed to something
else like K --> P.  A new table is required.

One could write a function to generate the translation table.  This would be
quite useful if the input strings were VERY large. At least I think so. This
could be profiled. shift_ord() is almost doing this.
'''

def shift_ord(ch, shift_n):
    assert(shift_n < 26)
    ch_ord = ord(ch)
    ch_sh  = ord(ch) + shift_n

    # Return char if outside the alphabet range
    if (ch_ord < ord('A')) or \
            (ch_ord > ord('Z') and ch_ord < ord('a')) or \
            (ch_ord > ord('z')):
        ch_shifted = ch
    # Return shifted ch handling wrapping

    # ABCDZ #$% abcdz %^&
    else:
        if ch_sh > ord('z'):
            delta = ch_sh - ord('z')
            ch_shifted = chr(ord('a') + delta - 1)
        elif ch_sh > ord('Z') and ch_sh < ord('a'):
            delta = ch_sh - ord('Z')
            ch_shifted =  chr(ord('A') + delta)
        else:
            ch_shifted = chr(ch_sh)

    return ch_shifted

def shift_msg(msg, shift):
    msg_shifted = ''
    for c in msg:
        msg_shifted += shift_ord(c, shift)
    return msg_shifted

def explore():
    '''
    Find a solution.
    '''
    msg_orig = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    msg_shifted = shift_msg(msg_orig, 2)

    print msg_orig
    print '\nShifted solution:'
    print msg_shifted

if __name__ == '__main__':
    explore()
