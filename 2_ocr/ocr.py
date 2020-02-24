#!/usr/bin/env python
"""
Find the characters only used once in long string and print the
ones used only once in order of appearance.
"""

import operator

def count_character_usage():
    '''
    Open input file and read.
    Return a dictionary with characters as keys
    and their counts as values.
    '''
    dic = {}
    with open('ocr_data.txt', 'r') as infile:
        for line in infile:
            for cha in line:
                try:
                    dic[cha] += 1
                except KeyError:
                    dic[cha] = 1
    return dic

def sort_for_least(dic):
    '''
    Return a list of sorted tuples each containing dic's
    key and value.
    '''
    return sorted(dic.items(), key=operator.itemgetter(1))

def find_least_used(ocr_list):
    '''Return a list of characters used once.'''
    least = []
    for tup in ocr_list:
        if tup[1] == 1:
            least.append(tup[0])
    return least

def write_least_used_in_order_used(least_list):
    '''
    Open in and out files.
    For each character that is used once, write it to outfile.
    This produces an outfile with all the characters
    used only once and in order of appearance.
    '''
    print('--->', least_list)
    with open('ocr.out', 'w') as outfile, open('ocr_data.txt', 'r') as infile:
        for line in infile:
            for cha in line:
                if cha in least_list:
                    outfile.write(cha)  # equality%

def explore():
    '''
    Find the solution.
    fixme: A better value data structure in count_dic would
    improve solution by not rereading the infile again.
    '''
    count_dic = count_character_usage()
    sorted_tups = sort_for_least(count_dic)
    least_used = find_least_used(sorted_tups)
    write_least_used_in_order_used(least_used)

if __name__ == '__main__':
    explore()

