#!/usr/bin/python3
def no_c(my_string):
    str = list(my_string)
    if 'C' in str:
        str.remove('C')
    elif 'c' in str:
        str.remove('c')
    return ''.join(str)
