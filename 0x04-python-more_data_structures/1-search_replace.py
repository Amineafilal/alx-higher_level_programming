#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def filtresearch(x):
        if x == search:
            return replace
        else:
            return x
    nombre_replace = list(map(filtresearch, my_list))
    return (nombre_replace)
