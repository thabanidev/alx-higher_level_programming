#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    """Safely prints out elements of a list

    Args:
        my_list (list, optional): List who's elements should be printed. Defaults to [].
        x (int, optional): Number of elements to print. Defaults to 0.
    Returns:
        int: Number of elements printed
    """
    if not my_list:
        return 0
    printed_count = 0
    try:
        for i, item in enumerate(my_list):
            if 0 <= i >= x:
                raise IndexError
            print(item, end="")
            printed_count += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_count
    