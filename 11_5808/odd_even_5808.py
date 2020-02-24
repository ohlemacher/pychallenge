#!/usr/bin/env python
"""
11: 5808
Given the image, which is obviously images mixed together somehow,
find the hidden message.  The hint is 'odd and even'.
"""

import mahotas as mh
import pylab

def explore(fname):
    """
    Read the img into an ndarray named img.
    Slice up the img.
    Throw away odd rows and odd columns.
    The answer is in what is left.
    """
    # img is an ndarray.
    img = mh.imread(fname)

    img_even = img[0::2, 0::2]
    pylab.imshow(img_even)
    pylab.show()


if __name__ == '__main__':
    FILE_NAME = 'cave.jpg'
    explore(FILE_NAME)
