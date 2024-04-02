#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        Result = fct(*args)
        return Result
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
