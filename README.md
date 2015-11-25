# pychallenge
Solutions for pythonchallenge.com puzzles.   Most are implemented in Python, but some are also solved in C++.

1. map
    - Problem:
        - Given an unreadable string and some hints, decode the message.
    - Hints:
        - 'What about making trans?
        - A photo:
            + K --> M
            + O --> Q
            + E --> G
    - Solution:
        The solution suggests using string.maketrans().  This works, but it
        requires a translation table.
        
        It also seems to have issues in Python 3. string.maketrans was deprecated and then removed.  Strings are not bytes. They are Unicode.
        
        I had considered using a dictionary for the table, but felt it makes reusability much harder. If the mapping K--> M changed to something else like K --> P, then a new table is required.
        
        One could write a function to generate the translation table.  This would be quite useful if the input strings were VERY large. At least I think so. This could be profiled. shift_ord() is almost ready to do this.

2. ocr
    - Problem:
        - Hidden in the html source is a large block of unreadable text.
    - Hints:
        - 'find rare characters in the mess below:'
    - Solution:
        Count the characters in the text block. The answer is the characters used once in the order they appear.

3. equality
    - Problem:
        - Find characters a block of text that are 
    - Hints:
        - RE
        - One small letter, surrounded by EXACTLY three big bodyguards on 
each of its sides.
    - Solution:
        - Use a RE to find the matches.
        - [^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+
