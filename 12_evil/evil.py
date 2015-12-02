#!/usr/bin/env python

'''
The evil page contains an image evil1.jpg. Guessing that there might be a '2',
we get an image that says "not .jpg, .gfx". evil2.gfx is also available.
evil3.jpg also exists but says "there are no more evils".

Now to figure out what evil2.gfx is...

jpeg magic number: ff d8 ff e0
first 16 bytes   : ff89 4789 ffd8 5049 50d8 ff4e 464e ffe0
skipping some    : ff          d8           ff          e0

Maybe we need to take one byte, skip four, repeat...?
Yes, the gfx is five images muxed together.
'''

from __future__ import print_function
import sys
import requests
import mahotas as mh
import pylab

def get_data(site, file_name, user='huge', passwd='file'):
    """
    Download the file.
    Return the content and status code.
    """
    response = requests.get('%s/%s' % (site, file_name),
                            auth=(user, passwd),
                            stream=True)
    if response.status_code != 200:
        return '', response.status_code
    return response.content, response.status_code

def handle_gfx_slice(offset, data):
    """
    Determine the image type, as indicated by its magic numer, of the slice.
    Create a image file with correct extension.
    Display the image using pylab.
    """
    print("\n=== ", offset, " ===", sep='')
    filtered_data = []
    for i in xrange(offset, len(data), 5):
        filtered_data.append(data[i])

    magic = ''.join("{:02x}".format(ord(c)) for c in filtered_data[:8:])
    if magic[0:8] == 'ffd8ffe0':
        ext = 'jpg'
    elif magic[0:16] == '89504e470d0a1a0a':
        ext = 'png'
    elif magic[0:12] == '474946383761' or magic[0:12] == '474946383961':
        ext = 'gif'
    else:
        ext = 'fail'
    print('magic:', magic)
    print('ext:', ext)

    # fixme: Factor this into a function
    with open('%s.%s' % (offset, ext), 'w') as out_file:
        for item in filtered_data:
            out_file.write(item)

    img = mh.imread("%s.%s" % (offset, ext))
    pylab.imshow(img)
    pylab.show()

def explore(data):
    """
    Demux and handle each of the 5 images within the data.
    Each image is a slice.
    """
    for i in range(0, 5):  # There are five images multiplexed within the gfx.
        try:
            handle_gfx_slice(i, data)
        except IOError as err:
            print("IOError:", err)
        except TypeError as err:
            # Image 3 has a compression error. gimp displays half of it.
            print("TypeError:", err)


if __name__ == '__main__':
    url = "http://www.pythonchallenge.com/pc/return"
    image_name = "evil2.gfx"

    image_data, status_code = get_data(url, image_name)
    if status_code != 200:
        print('Error: Download of', image_name, 'failed:', status_code)
        sys.exit(1)

    explore(image_data)

