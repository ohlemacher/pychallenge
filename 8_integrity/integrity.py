#!/usr/bin/env python

"""8: integrity"""

from __future__ import print_function
import bz2

def explore():
    """Explore solutions"""
    # Found in page source
    username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    passwd = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    username_inf = bz2.decompress(username)
    passwd_inf = bz2.decompress(passwd)

    print('user  :', username_inf.decode())
    print('passwd:', passwd_inf.decode())

if __name__ == '__main__':
    explore()

