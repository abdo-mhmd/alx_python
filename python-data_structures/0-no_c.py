#!/usr/bin/python3
def no_c(my_string):
    st = ''
    for c in my_string:
        if c.lower() != 'c':
            st += c
    return (st)
