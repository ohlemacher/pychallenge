# pychallenge
Solutions for pythonchallenge.com puzzles.   Most are implemented in Python, but some are also solved in C++.

1. Think Twice
- Problem:
    - Given an unreadable string and three hints, decode the message.
- Hints:
    - 'What about making trans?
    - A photo
        + K --> M
        + O --> Q
        + E --> G
- Solution:
The solution suggests using string.maketrans().  This works, but it
requires a translation table.

It also seems to have issues in Python 3 string.maketrans was deprecated and then removed.  Strings are not bytes. They are Unicode.

I had considered using a dictionary for the table, but felt it makes reusability much harder if the mapping K--> M changed to something else like K --> P.  A new table is required.

One could write a function to generate the translation table.  This would be quite useful if the input strings were VERY large. At least I think so. This could be profiled. shift_ord() is almost doing this.
