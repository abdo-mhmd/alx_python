#!/usr/bin/python3
import sys

def print_arguments():
    argv = sys.argv[1:]
    num_args = len(argv)

    print("{}".format(num_args), end="")
    if num_args == 0:
        print(".", end="\n")
    elif num_args == 1:
        print(" argument:\n1: {}".format(argv[0]), end="\n")
    else:
        print(" arguments:",end="\n")

        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()
