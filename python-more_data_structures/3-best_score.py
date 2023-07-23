#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        hight_score = max(list(a_dictionary.values()))
        for key in a_dictionary:
            if a_dictionary.get(key) == hight_score:
                return (key)
