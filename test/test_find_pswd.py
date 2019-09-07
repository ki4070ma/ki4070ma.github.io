#!/usr/bin/env python

from change_pswd_func.find_pswd import find_pswd, load_system_pswd


class TestFindPswd(object):

    # TestIdx: 1
    def test_find_pswd_found(self):
        pswd = load_system_pswd()[-1]
        assert find_pswd(pswd)

    # TestIdx: 2
    def test_find_pswd_not_found(self):
        pswd = load_system_pswd()[-1]*2
        assert not find_pswd(pswd)
