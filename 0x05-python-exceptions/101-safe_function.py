#!/usr/bin/python3
def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex))
    return result
