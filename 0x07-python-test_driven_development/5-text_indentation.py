#!/usr/bin/python3
""" Module holds text_indentation function. """


def text_indentation(text):
    """ text_indentation
    Will print a string while printing two newlines after . ? and :
    Args:
        text (string): string to print
    """
    skip = False

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in range(len(text)):
        if skip:
            skip = False
            continue
        if text[c] is ":" or text[c] is "." or text[c] is "?":
            print("{}\n\n".format(text[c], "c"), end='')
            skip = True
        else:
            print("{}".format(text[c], "c"), end='')
