#!/usr/bin/env python

from Levenshtein import distance  # type: ignore

from .constants import SIMILARITY_THRESHOLD


def similar(string1: str, string2: str) -> bool:
    '''Check two strings similarity

    Calculate distance between two strings and compare distance with threshold

    [Change password requirement]
    3. password is not similar to old password < 80% match.

    Returns:
        bool: True if two strings are similar otherwise False

    '''

    if type(string1) is not str or type(string2) is not str:
        raise TypeError('Args need to be str type.')

    print('\n[string1]: {}'.format(string1))  # '\n' is for pytest output
    print('[string2]: {}'.format(string2))
    normalized_distance = distance(string1, string2) / max(len(string1), len(string2))
    return 1 - normalized_distance > SIMILARITY_THRESHOLD
