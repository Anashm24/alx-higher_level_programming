#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_list = list(a_dictionary.keys())
    for i in a_list:
        if i == key:
            del a_dictionary[key]
        else:
            return
