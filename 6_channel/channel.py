#!/usr/bin/env python

"""6: Channel"""
# hint1: start from 90052
# hint2: answer is inside the zip

from __future__ import print_function
import sys
import requests
import zipfile
import re


def get_zip_file(url, name):
    """Get the url file and write it to disk."""
    response = requests.get(url)
    zip_data = response.content
    if response.status_code != 200:
        print("Error: Failed to get channel.zip")
        sys.exit(1)
    with open(name, 'w') as channel_zip:
        channel_zip.write(zip_data)

def follow_file(zfile, name, comments=None):
    """
    Each file points to the next and has a comment.
    Collect the comment. Follow to the next file recursively.
    """
    # The first call, before the recursion starts, needs to create this list.
    if comments is None:
        comments = []

    try:
        content = zfile.read(name)
        comment = zfile.getinfo(name).comment
        comments.append(comment)

        match = re.search('Next nothing is ([0-9]+)', content)
        if not match:
            print('An interesting file was found:', name)
            print(content)
            return

        next_file = match.group(1) + '.txt'
        follow_file(zfile, next_file, comments)
    except KeyError:
        print('Error: Failed to read', name)
        sys.exit(2)

    return comments

def explore():
    """Explore."""
    channel_name = 'channel.zip'
    channel_url = 'http://www.pythonchallenge.com/pc/def/%s' % channel_name

    get_zip_file(channel_url, channel_name)
    zfile = zipfile.ZipFile(channel_name)

    follow_file(zfile, 'readme.txt')

    comments = follow_file(zfile, '90052.txt')
    print(''.join(comments))


if __name__ == '__main__':
    explore()
