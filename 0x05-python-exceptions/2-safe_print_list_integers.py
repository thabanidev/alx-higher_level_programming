#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers

    Args:
        my_list (list): List of elements to print.
        x (int): Number of elements to print.

    Returns:
        int: Number of elements printed.
    """
    number_of_elements_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number_of_elements_printed += 1
        except (IndexError, ValueError, TypeError):
            continue
    print()
    return number_of_elements_printed
