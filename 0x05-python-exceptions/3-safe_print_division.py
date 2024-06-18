#!/usr/bin/python3
def safe_print_division(a, b):
    """Prints the quotient of two numbers safely

    Args:
        a (int): first operand
        b (int): second perand

    Returns:
        int: Quotient of a and b otherwise None.
    """
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:", result)
        return result
