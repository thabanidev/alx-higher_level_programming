#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer.

    Args:
        value (any): The value to print.

    Returns:
        bool: True if the value was printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
