#!/usr/bin/env python

"""
10: Bull
ref: https://en.wikipedia.org/wiki/Look-and-say_sequence
"""

from __future__ import print_function
import re

def look_and_say(seed):
    '''Execute look and say algo on seed.'''
    seq = str(seed)
    say = []
    last_first = ''
    for j in range(0, len(seq)):
        first = seq[j]
        if first == last_first:
            continue
        rest = str(seq[j:])
        matches = re.search(r"^(%s+)" % first, rest)
        if not matches:
            print(f"Error: no matches: {seed}")
            return
        this_match = matches.groups()[0]
        say.append(str(len(this_match)) + this_match[0])
        last_first = this_match[0]
    #print("{seed} --> {say}")
    return ''.join(say)

def len_at_n_iters(iterations):
    '''Run through the n iterations.'''
    seed = 1
    for i in range(0, iterations):
        seed = look_and_say(seed)
    print(f"Answer: {i} --> {seed} --> {len(seed)}")

def explore():
    '''a = [1, 11, 21, 1211, 111221,'''
    #say = look_and_say(111221)
    #print('say:', ''.join(say))
    len_at_n_iters(30)

if __name__ == '__main__':
    explore()
