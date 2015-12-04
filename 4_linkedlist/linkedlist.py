#!/usr/bin/env python

"""4: Linkedlist"""

from __future__ import print_function
import sys
import requests
import re

def get_next_link(url, link):
    """Get the url and link. Find the next link from the content."""
    response = requests.get("%s%s" % (url, link))
    if response.status_code != 200:
        print("Error: Failed to get next nothing at %s%s" % (url, link))
        sys.exit(1)
    content = response.content
    # print('content:', content)

    # Match 'nothing is <some number>'
    match = re.search('nothing is ([0-9]+)', content)
    if match:
        next_link = match.group(1)
    else:
        # Match divide by two content. Return current link / 2.
        match_divide_by_2 = re.search('Yes. Divide by two and keep going.',
                                      content)
        if match_divide_by_2:
            assert int(link) % 2 == 0
            next_link = str(int(link) / 2)
        else:
            print('An interesting link was found:', )
            print('\t', content)
            sys.exit(0)
    # print("%s --> %s" % (link, next_link))
    return next_link

def explore():
    """Explore solution."""
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    link = "12345"  # Start link from puzzle page.
    for i in xrange(0, 400):  # See hints
        link = get_next_link(url, link)


if __name__ == '__main__':
    explore()

