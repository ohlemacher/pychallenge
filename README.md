# pychallenge
Solutions for pythonchallenge.com puzzles.   Most are implemented in Python, but some are also solved in C++.

1. map (aka think_twice)
    - Problem:
        - Given an unreadable string and some hints, decode the message.
    - Hints:
        - 'What about making trans?
        - A photo:
            + K --> M
            + O --> Q
            + E --> G
    - Solution:
        The solution suggests using string.maketrans().  This works, but it requires a translation table.

        It also seems to have issues in Python 3. string.maketrans was deprecated and then removed.  Strings are not bytes. They are Unicode.

        I had considered using a dictionary for the table, but felt it makes reusability much harder. If the mapping K--> M changed to something else like K --> P, then a new table is required.

        One could write a function to generate the map or translation table. This would be quite useful if the input strings were VERY large. At least I think so. Profiling would determine this. shift_ord() is almost ready to do this.
        Answer: ocr

2. ocr
    - Problem:
        - Hidden in the html source is a large block of unreadable text.
    - Hints:
        - 'find rare characters in the mess below:'
    - Solution:
        - Count the characters in the text block.
        - The answer is the characters used once in the order they appear.
        - Answer: equality

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
        - Answer: linkedlist

4. linkedlist
    - Problem: Start at a url and follow the links until the end. There are a couple of special cases to handle with re.
    - Hints:
        - follow the chain
        - urllib may help. DON'T TRY ALL NOTHINGS, since it will never end.
        - 400 times is more than enough.
        - The starting link is 12345"
    - Solution:
        - Use requests to tranverse the links. Use re to find the next link.
        - Answer: peak

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
        - Answer: channel

6. channel
    - Problem:
        - Look at the picture and source and realize that a zip file must be downloaded and analyzed.
    - Hints:
        - The picture is of a zipper.
        - start from 90052.
        - answer is inside the zip.
    - Solution:
        - Use requests to download channel.zip.
        - Use recursion to follow each file in the zip file to the next.
        - Collect each file's comments while following.
        - Stop recursive calls once an interesting file is found.
        - Print the comments.
        - Comments are a banner: HOCKEY.
            - Another hint: 'it's in the air. look at the letters.'
            - The banner is formed from the banner characters.
            - Answer: oxygen

7. oxygen
    - Problem:
        - A picture of a stream with a line of gray blocks varying in intensity.
    - Hints:
        - Page title is 'smarty'.
    - Solution:
        - Get the image using requests.
        - Use the mahotas image processing library to create a numpy ndarray with the pixel data.
        - The gray blocks have some information.
        - Find them. Being gray, they each have equal values for red, green and blue.
        - The gray values map to ASCII characters. Use chr() to convert to a character.
        - Note: The blocks each have many pixels, horizontally and vertically (it is a block). This leads to repeating strings and characters within the strings. Attempting to dedup can cause issues. Take care with strings like 110 which could be incorrectly deduped to 10.
        - Answer: integrity

8. integrity
    - Problem:
        - We have a picture of a bee with a hyperlink. When clicked, we a prompted for credentials.
    - Hints:
        - The page source contains:
            - un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
            - pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    - Solution:
        - The un and pw strings start with 'BZ'. They are compressed with bzip compression.
        - Use the bz2 module to decompress each. Print the results.
        - Answer:
            - user  : huge
            - passwd: file
            - Authentication leads to good.html

9. good
    - Problem:
        - We have a picture of a mountain view over water.
        - There are some seeminly randomly placed black dots.
    - Hints:
        - Connect the dots
        - Page source contains:
            - first+second=?
            - Two strings of numbers named first and second. They have different lengths.
    - Solution:
        - first and second are of different lengths so they cannot be coordinates used together.
        - They are instead represent two lines. The numbers are coordinates concatenated, e.g. [x0, y0, x1, y1...].
        - Use zip() to create a list of coordinate tuples for both first and second.
        - Use the PIL library to draw both lines.
        - Answer: The lines form the outline of a cow but it has horns so it is really a bull.

10. bull
    - Problem:
    - Hints:
    - Solution:
