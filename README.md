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
        - Find characters in a block of text that match.
    - Hints:
        - RE
        - One small letter, surrounded by EXACTLY three big bodyguards on
each of its sides.
    - Solution:
        - Use a RE to find the matches.
        - [^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+

4. linkedlist
    - Problem: Start at a url and follow the links until the end. There are a couple of special cases to handle with re.
    - Hints:
        - follow the chain
        - urllib may help. DON'T TRY ALL NOTHINGS, since it will never end.
        - 400 times is more than enough.
        - The starting link is 12345"
    - Solution:
        - Use requests to tranverse the links. Use re to find the next link.

5. peak
    - Problem:
        - The page source implies there is a source file to get. Figure out what to do with it.
    - Hints:
        - peakhell src="banner.p
        - peakhell sounds a bit like pickle, but this was not so obvious.
    - Solution:
        - Use requests to get banner.p.
        - Figure out it is a pickle file.
        - Demarshal the file using the pickle module.
        - Print the text.  It contains lines of tuples (# or a space, multiplier), readable once printed.

6. channel
    - Problem:
        - Look at the source and realize that the zip module is required.
    - Hints:
        - The picture is of a zipper.
        - start from 90052.
        - answer is inside the zip.
    - Solution:
        - Use requests to download channel.zip.





