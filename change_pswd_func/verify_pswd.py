#!/usr/bin/env python

import re

from .constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH,
    SP_CHARS
)
from .log import LogMsgVerifyPswd


def verify_pswd(pswd: str) -> bool:
    print('\n[pswd]: {}'.format(pswd))  # '\n' is for pytest output
    if _check_length(pswd):
        print('Password length is {}.'.format(len(pswd)))
        print(LogMsgVerifyPswd.INVALID_LENGTH)
    elif _include_invalid_char(pswd):
        print(LogMsgVerifyPswd.INVALID_CHAR)
    elif _include_not_all_patterns(pswd):
        print(LogMsgVerifyPswd.NOT_ALL_PATTERNS)
    elif _include_over_continuous_same_chars(pswd):
        print(LogMsgVerifyPswd.OVER_CONTINUOUS_SAME_CHARS)
    elif _include_over_sp_char_num(pswd):
        print(LogMsgVerifyPswd.OVER_SP_CHAR_NUM)
    elif _include_num_more_than_half_of_length(pswd):
        print(LogMsgVerifyPswd.MORE_THAN_HALF_OF_LENGTH)
    else:
        print(LogMsgVerifyPswd.VALID)
        return True
    return False


def _check_length(pswd: str) -> bool:
    '''
    [Password requirement] 1. At least 18 alphanumeric characters and list of special chars !@#$&*
    '''
    return len(pswd) < MIN_VALID_LENGTH or len(pswd) > MAX_VALID_LENGTH


def _include_invalid_char(pswd: str) -> bool:
    '''
    [Password requirement] 1. At least 18 alphanumeric characters and list of special chars !@#$&*
    '''
    for x in pswd:
        # x.isalnum() unavailable for Hiragana, Kanji, etc
        if not bool(re.search('[0-9a-zA-Z]', x)) and x not in SP_CHARS:
            return True
    return False


def _include_not_all_patterns(pswd: str) -> bool:
    '''
    [Password requirement] 2. At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
    '''
    upper_flg = False
    lower_flg = False
    num_flg = False
    special_flg = False
    for x in pswd:
        if x.isupper():
            upper_flg = True
        elif x.islower():
            lower_flg = True
        elif x.isnumeric():
            num_flg = True
        elif x in SP_CHARS:
            special_flg = True
        if upper_flg and lower_flg and num_flg and special_flg:
            return False
    return True


def _include_over_continuous_same_chars(pswd: str) -> bool:
    '''
    [Password requirement] 3. No duplicate repeat characters more than 4
    '''
    count = 1
    prev_char = pswd[0]
    for x in list(pswd)[1:]:
        if x == prev_char:
            count += 1
        else:
            # Reset
            count = 1
            prev_char = x
        if count > MAX_CHAR_CONTINUOUS_NUM:
            return True
    return False


def _include_over_sp_char_num(pswd: str) -> bool:
    '''
    [Password requirement] 4. No more than 4 special characters
    '''
    count = 0
    for c in SP_CHARS:
        count += pswd.count(c)
    return count > MAX_SP_CHAR_NUM


def _include_num_more_than_half_of_length(pswd: str) -> bool:
    '''
    [Password requirement] 5. 50 % of password should not be a number
    '''
    count = 0
    for c in pswd:
        if c.isnumeric():
            count += 1
    return count >= len(pswd) / 2.0
