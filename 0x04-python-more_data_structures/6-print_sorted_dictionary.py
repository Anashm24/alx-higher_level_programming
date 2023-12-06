#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dic = sorted(list(a_dictionary.keys()))
    for key in list_dic:
        print(f"{key}: {a_dictionary.get(key)}")
