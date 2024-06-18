#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element of two lists

    Args:
        my_list_1 (list): list of numbers
        my_list_2 (list): list of numbers
        list_length (int): length of the lists

    Returns:
        list: list of size list_length with all division results
    """
    my_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError) as ex:
            result = 0
            if isinstance(ex, ZeroDivisionError):
                print("division by zero")
            elif isinstance(ex, TypeError):
                print("wrong type")
            elif isinstance(ex, IndexError):
                print("out of range")
        finally:
            my_list.append(result)
    return my_list
