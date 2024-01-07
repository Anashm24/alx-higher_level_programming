#!/usr/bin/python3
"""defines a  function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    
        text: is a string
        Raises:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for mark in ".?:":
        text = text.replace(mark, mark + "\n\n")
    
    print("\n".join(line.strip() for line in text.split("\n")))
