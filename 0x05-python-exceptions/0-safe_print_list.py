#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    """Safely prints out elements of a list

    Args:
        my_list (list, optional): List who's elements should be printed. Defaults to [].
        x (int, optional): Number of elements to print. Defaults to 0.
    """
    if not my_list:
        return 0
    printed_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_count
    