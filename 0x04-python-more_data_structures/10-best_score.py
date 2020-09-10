#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # With this I take the first key of the dictionary
        winner = list(a_dictionary.keys())[0]

        # With this I take the first value of the dictionary
        bigger = list(a_dictionary.values())[0]

        for key in a_dictionary.keys():
            if a_dictionary[key] > bigger:
                bigger = a_dictionary[key]
                winner = key
        return winner
    else:
        return None
