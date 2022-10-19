#!/usr/bin/python3
""" Text Indentation

Prints a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):
    """Indentation function
    
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (string) : this is the input sentence to be indented.
    """

    new = ''
    """a string to hold out indented text"""

    sl = text.split()
    """a list containing our text whitout whitespaces"""
    
    for i in range(len(sl)):
        new += sl[i]
        if sl[i][-1] in ['.', '?', ':']:
            new += '\n\n'
        elif sl[i] is not sl[-1]:
            new += ' '
    print(new, end="")