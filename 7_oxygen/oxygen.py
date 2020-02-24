#!/usr/bin/env python

"""
Solution to #7 oxygen at pythonchallenge.com

Mac: `brew install freeimage`

"""

from __future__ import print_function
import requests
import mahotas as mh
# import pylab
import pprint

def get_image(site, image_file):
    """Download the image."""
    response = requests.get('%s/%s' % (site, image_file))
    print(f"status code: {response.status_code}")
    if response.status_code != 200:
        print('Error: get image failed.')
    with open(image_file, 'wb') as out:
        out.write(response.content)

def explore_image(image_file):
    """
    Find the gray blocks.
    Gray blocks have r==g==b values.
    Convert the value to a char.
    Collect and print the chars.
    """
    img = mh.imread(image_file)
    #pylab.imshow(img)
    #pylab.show()
    shape = img.shape
    pprint.pprint(shape)
    values = []
    for row in range(0, shape[0]):
        for col in range(0, shape[1]):
            pixel = img[row, col]
            if pixel[0] == pixel[1] and pixel[1] == pixel[2]:
                # pixel is gray
                if pixel[0] >=32 and pixel[0] <= 127:
                    char = chr(pixel[0])
                    values.append(char)

    # Only use one of each repeated value (block of gray).
    filtered_values = []
    for i, v in enumerate(values):
        if i == 0:
            filtered_values.append(v)
        elif v != values[i-1]:
            filtered_values.append(v)

    print("values:")
    pprint.pprint(''.join(values))

    print("filtered values:")
    pprint.pprint(''.join(filtered_values))

    # Answer:
    # smart guy, you made it. the next level is
    # [105, 110, 116, 101, 103, 114, 105, 116, 121]

    # Make an ascii string
    answer = ''.join([chr(x) for x in
                      [105, 110, 116, 101, 103, 114, 105, 116, 121]])
    print(f"answer: {answer}")

def main():
    """
    Find the hidden message in the image.
    """
    site = 'http://pythonchallenge.com/pc/def'
    image_file = 'oxygen.png'
    get_image(site, image_file)
    explore_image(image_file)


if __name__ == '__main__':
    main()
