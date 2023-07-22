#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b != 0:
            return (a / b)
        else:
            return (None)
    except ZeroDivisionError as ex:
        print(ex)
    finally:
        if b != 0:
            print("Inside result: {}".format(a / b))
        else:
            print("Inside result: {}".format(None))
