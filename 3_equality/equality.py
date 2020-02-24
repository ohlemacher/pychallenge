#!/usr/bin/env python

'''
Find lower case characters surrounded by exactly three upper case
characters on each side.

For unittests, run script.
For solution, run interactively:
    >>> import equality
    >>> equality.explore()
'''

import pprint
import re
import unittest

def file_to_string():
    '''Read the file into a string.'''
    strg = ''
    with open('equality.txt', 'r') as infile:
        for line in infile:
            for cha in line:
                if cha != '\n':
                    strg += cha
    return strg

def find_guarded_matches(strg):
    '''
    Use a regex to find the guarded chars.
    '''
    guard_re = re.compile(r"""
                          (^|[^A-Z]{1}) # Beginning or 3 non-uppercase
                          [A-Z]{3}      # Three uppercase (guard)
                          ([a-z]{1})    # One lowercase
                          [A-Z]{3}      # Three uppercase (guard)
                          ($|[^A-Z]{1}) # End or 3 non-uppercase
                          """,
                          re.VERBOSE)
    matches = guard_re.findall(strg)

    # Since three groups are used in the regex, tuples are returned.
    # We only want the middle one.
    answer = ''
    for tup in matches:
        answer += tup[1]
    return answer

def explore():
    '''Find the solution. Run iteractively.'''
    strg = file_to_string()
    print(find_guarded_matches(strg))

class EqualityTest(unittest.TestCase):
    '''Unit test set.'''
    def test_start_match(self):
        '''Test match at start of strg.'''
        strg = "AAAxBBBooCCCyDDDo"
        answer = 'xy'
        result = find_guarded_matches(strg)
        self.assertTrue(result==answer)

    def test_middle_match(self):
        '''Test match in middle of strg.'''
        strg = "mNoAAAxBBBooCCCyDDDmNo"
        answer = 'xy'
        result = find_guarded_matches(strg)
        self.assertTrue(result==answer)

    def test_end_match(self):
        '''Test match at end of strg.'''
        strg = "ooAAAxBBBooCCCyDDD"
        answer = 'xy'
        result = find_guarded_matches(strg)
        self.assertTrue(result == answer)

    def test_no_match(self):
        '''Test no matches in strg.'''
        strg = "ooAaAxBBBooCCCyDdD"
        answer = ''
        result = find_guarded_matches(strg)
        self.assertTrue(result==answer)

if __name__ == '__main__':
    # A real app would use argparse to optionally exec the unit tests.
    unittest.main()

