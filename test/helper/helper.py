#!/usr/bin/env python

from change_pswd_func.constants import (
    MIN_VALID_LENGTH,
    SIMILARITY_THRESHOLD,
    SP_CHARS
)

CHAR_UPPER_1 = 'A'

CHAR_UPPER_2 = 'C'

CHAR_LOWER = 'b'

CHAR_NUM = '1'

PSWD_LENGTH = 100


def pswd_generator(pswd_base='', length=MIN_VALID_LENGTH,
                   incl_upper_char=True, incl_lower_char=True, incl_num=True, incl_sp_char=True):
    '''Generate password

    To generate password along to points in below file
    https://docs.google.com/spreadsheets/d/1Gq1EUD5i_Ko0uE9PCUINHnwNm5oDvesw5OMNhHfZT14/edit#gid=0

    However, need to use `pswd_base` to meet 'Duplicate repeat char' and 'Ratio of num in pswd'
    Need to know how password is generated by repeating `base_strings` in below codes.
    TODO: Make easy to understand how password is generated along to args

    Args:
        pswd_base(str): Used string at the HEAD of password
        length(int): Password length in total
        incl_upper_char(bool): Flag to include upper char in password.
            If True, added 1 upper char to `base_strings`
        incl_lower_char(bool): Flag to include lower char in password.
            If True, added 1 lower char to `base_strings`
        incl_num(bool): Flag to include numeric in password.
            If True, added 1 numeric to `base_strings`
        incl_sp_char(bool):Flag to include sp char in password.
            If True, used sp char at the TAIL of password

    Returns:
         str: Genrated password
    '''

    base_str = ''
    base_str += CHAR_UPPER_1 if incl_upper_char else ''
    base_str += CHAR_LOWER if incl_lower_char else ''
    base_str += CHAR_NUM * len(base_str) if incl_num else ''
    for i in range(length-len(pswd_base)):
        pswd_base += base_str[i % len(base_str)]
    if incl_sp_char:
        pswd_base = pswd_base[:-1] + SP_CHARS[0]
    return pswd_base


def pswd_changer(pswd, diff_ratio=(1-SIMILARITY_THRESHOLD+0.01)):
    '''

    Default 79% match.
    As caution, `diff_ratio` works well for more than or equal to 100 password length.
    If length is less than 100, set `diff_ratio` bigger value.

    :param pswd:
    :param diff_ratio:
    :return:
    '''
    print(int(len(pswd) * diff_ratio))
    return pswd.replace(CHAR_UPPER_1, CHAR_UPPER_2, int(len(pswd) * diff_ratio))


def strings_generator_same_tail(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Two strings has the same strings at TAIL.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: XXXooooooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: XXoooooooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: Xooooooooo
            str2: oooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''

    len1 = int(length*SIMILARITY_THRESHOLD + str_diff_num)
    str1 = '{}{}'.format('X' * (length - len1), 'o' * len1)
    str2 = 'o' * length
    return str1, str2


def strings_generator_same_center(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Two strings has the different strings at CENTER.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: ooooXXXooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: ooooXXoooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: ooooXooooo
            str2: oooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''

    len1 = int(length * SIMILARITY_THRESHOLD + str_diff_num)
    str1 = '{}{}{}'.format('o' * int(len1 / 2), 'X' * (length - len1), 'o' * (len1 - int(len1 / 2)))
    str2 = 'o' * length
    return str1, str2


def strings_generator_same_head(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Two strings has the same strings at HEAD.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: oooooooXXX
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: ooooooooXX
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: oooooooooX
            str2: oooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''

    len1 = int(length * SIMILARITY_THRESHOLD + str_diff_num)
    str1 = '{}{}'.format('o' * len1, 'X' * (length - len1))
    str2 = 'o' * length
    return str1, str2


def strings_generator_matched_char_mixed(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Matched strings are within strings.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: oXoXoXoooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: oXoXoooooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: oXoooooooo
            str2: oooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''

    len1 = int(length * SIMILARITY_THRESHOLD + str_diff_num)
    char_list = ['o'] * length
    for i in range(length - len1):
        if char_list[2 * i + 1] != 'o':
            char_list[2 * i + 1] = 'X'
        else:
            char_list[2 * i] = 'X'
    str1 = ''.join(char_list)
    str2 = 'o' * length
    return str1, str2


def strings_generator_dest_str_longer(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Destination string is longer than source string.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: ooooooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: oooooooo
            str2: oooooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: ooooooooo
            str2: oooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''

    str1 = 'o'*int(length * SIMILARITY_THRESHOLD + str_diff_num)
    str2 = 'o'*length
    return str1, str2


def strings_generator_src_string_longer(str_diff_num, length=PSWD_LENGTH):
    '''Check similarity between two strings with `str_diff_num`.

    One string has difference which is timed by `SIMILARITY_THRESHOLD`
    and added `str_diff_num`.
    Destination string is longer than source string.

    Example:
        `SIMILARITY_THRESHOLD` is 0.8.
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 1
            str1: oooooooooo
            str2: ooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: 0
            str1: oooooooooo
            str2: oooooooo
        Below strings will be returned with `LENGTH`:10, `str_diff_num`: -1
            str1: oooooooooo
            str2: ooooooooo

    Args:
        str_diff_num(int): additional the number of string difference

    Returns:
        str, str: Generated two strings
    '''
    str1 = 'o'*length
    str2 = 'o'*int(length * SIMILARITY_THRESHOLD + str_diff_num)
    return str1, str2