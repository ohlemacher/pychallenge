#!/usr/bin/env python

"""6: Channel"""
# hint1: start from 90052
# hint2: answer is inside the zip

from __future__ import print_function
import sys
import requests
import zipfile
import re
import pickle

def get_zip_file(url, name):
    """Get the url file and write it to disk."""
    response = requests.get(url)
    zip_data = response.content
    if response.status_code != 200:
        print("Error: Failed to get channel.zip")
        sys.exit(1)
    with open(name, 'wb') as channel_zip:
        channel_zip.write(zip_data)

def follow_file(zfile, name, comments=None):
    """
    Each file points to the next and has a comment.
    Collect the comment. Follow to the next file recursively.
    """
    if not comments:
        comments = []

    # The first call, before the recursion starts, needs to create this list.
    try:
        #print(f"== Examining {name}")
        content = str(zfile.read(name))
        comment = zfile.getinfo(name).comment.decode()

        #print(f"content: {content}")
        #print(f"comment: {comment}")

        match = re.search('Next nothing is ([0-9]+)', content)
        if not match:
            print(f'An interesting file was found: {name}')
            print(content)
            return comments
        else:
            comments.append(comment)

        next_file = f"{match.group(1)}.txt"
        follow_file(zfile, next_file, comments)
        return comments
    except KeyError:
        print(f'Error: Failed to read {name}')
        sys.exit(2)

def explore():
    """Explore."""
    channel_name = 'channel.zip'
    channel_url = f"http://www.pythonchallenge.com/pc/def/{channel_name}"

    get_zip_file(channel_url, channel_name)
    zfile = zipfile.ZipFile(channel_name)

    follow_file(zfile, 'readme.txt')

    comments = follow_file(zfile, '90052.txt')
    print(f"comments: \n{''.join(comments)}")


if __name__ == '__main__':
    explore()
