#!/usr/bin/python3
multiply_list_map = lambda my_list=[], number=0: list(map(lambda x: x * number, my_list or []))
