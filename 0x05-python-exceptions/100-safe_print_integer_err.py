#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer, but raises an error if the value is not an integer.

    Args:
        value (any): The value to print.

    Returns:
        bool: True if the value is an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
