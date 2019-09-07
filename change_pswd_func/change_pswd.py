#!/usr/bin/env python

from .check_similarity import similar
from .find_pswd import find_pswd
from .log import LogMsgChangePaswd
from .verify_pswd import verify_pswd


def change_pswd(old_pswd: str, new_pswd: str) -> bool:
    if not find_pswd(old_pswd):
        '''
        [Change password requirement] 1. Old password should match with system
        '''
        print(LogMsgChangePaswd.INVALID_OLD_PSWD)
    elif not verify_pswd(new_pswd):
        '''
        [Change password requirement] 2. New password should be a valid password
        '''
        print(LogMsgChangePaswd.INVALID_NEW_PSWD)
    elif similar(old_pswd, new_pswd):
        '''
        [Change password requirement] 3. password is not similar to old password < 80% match.
        '''
        print(LogMsgChangePaswd.SIMILAR_TO_OLD_ONE)
    else:
        print(LogMsgChangePaswd.SUCCESS)
        return True
    return False
