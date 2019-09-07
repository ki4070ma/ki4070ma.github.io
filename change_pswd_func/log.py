#!/usr/bin/env python

from typing import Generic, TypeVar

from .constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH
)

T = TypeVar('T')


class LogMsgVerifyPswd(Generic[T]):
    # TODO Can be used these msg to check which message is shown when validation is failed on unit test

    INVALID_LENGTH = '[NG] The length needs to be from {} to {}.'.format(MIN_VALID_LENGTH, MAX_VALID_LENGTH)

    INVALID_CHAR = '[NG] Included invalid char'

    NOT_ALL_PATTERNS = "[NG] All necessary patterns aren't included"

    OVER_CONTINUOUS_SAME_CHARS = '[NG] Included continous more than {} same chars'.format(MAX_CHAR_CONTINUOUS_NUM)

    OVER_SP_CHAR_NUM = '[NG] Included more than {} special characters'.format(MAX_SP_CHAR_NUM)

    MORE_THAN_HALF_OF_LENGTH = '[NG] 50 % of password should not be a number'

    VALID = '[OK] Valid password'


class LogMsgChangePaswd(Generic[T]):
    # TODO Can be used these msg to check which message is shown when validation is failed on unit test

    INVALID_OLD_PSWD = '[NG] Could not find old password in the system'

    INVALID_NEW_PSWD = '[NG] Could not change password due to invalid new password'

    SIMILAR_TO_OLD_ONE = '[NG] Could not change password due to similar to previous one'

    SUCCESS = '[OK] Changed password successfully'
