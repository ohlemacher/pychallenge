#!/usr/bin/env python
"""pythonchallenge.com puzzle 4, peak"""

from __future__ import print_function
import requests
import pickle

def main():
    """
    Get the data, banner.p, using a request.
    Data is pickled, so load the stream.
    Each line is a list of tuples (space/hash, multiplier).
    Each line is 95 chars long.
    Print the lines.
    A word is displayed.
    """
    print('4: peaks')
    response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
    if not response.status_code == 200:
        print('Error: Request for banner.p failed')
    else:
        # print(response.text)
        data = pickle.loads(response.text)
        # for line in data:
        #     print(line)
        for line in data:
            print(''.join([atom[0] * atom[1] for atom in line]))

if __name__ == '__main__':
    main()
