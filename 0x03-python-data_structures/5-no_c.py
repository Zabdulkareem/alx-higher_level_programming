#!/usr/bin/python3


def no_c(my_string):
    my_string = list(my_string.lower())
    for char in my_string:
        if 'c' in my_string:
            my_string.remove('c')
    return ("".join(my_string))
