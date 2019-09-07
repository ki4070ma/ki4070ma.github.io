#!/usr/bin/env python

from test.helper.helper import pswd_changer, pswd_generator

import pytest  # type: ignore

from change_pswd_func.change_pswd import change_pswd
from change_pswd_func.constants import (
    MAX_CHAR_CONTINUOUS_NUM,
    MAX_SP_CHAR_NUM,
    MAX_VALID_LENGTH,
    MIN_VALID_LENGTH,
    SIMILARITY_THRESHOLD,
    SP_CHARS
)
from change_pswd_func.find_pswd import load_system_pswd


class TestChangePasswd(object):

    # TestIdx: 1, 3, 5
    # [Old, new password length]: Valid various lengths
    # [Similarity] Similar
    @pytest.mark.parametrize('length', [MIN_VALID_LENGTH, 100, MAX_VALID_LENGTH])
    @pytest.mark.parametrize('add_diff_ratio', [-0.1, 0])  # >=80% matching
    def test_change_pswd_valid_length_similar(self, length, add_diff_ratio):
        old_pswd = pswd_generator(length=length)
        new_pswd = pswd_changer(old_pswd, diff_ratio=(1-SIMILARITY_THRESHOLD+add_diff_ratio))
        assert not change_pswd(old_pswd, new_pswd)

    # TestIdx: 2, 4, 6
    # [Old, new password length]: Valid various lengths
    # [Similarity] Dissimilar
    @pytest.mark.parametrize('length', [MIN_VALID_LENGTH, 100, MAX_VALID_LENGTH])
    @pytest.mark.parametrize('add_diff_ratio', [0.1])  # <80% matching
    def test_change_pswd_valid_length_dissimilar(self, length, add_diff_ratio):
        old_pswd = pswd_generator(length=length)
        new_pswd = pswd_changer(old_pswd, diff_ratio=(1-SIMILARITY_THRESHOLD+add_diff_ratio))
        assert change_pswd(old_pswd, new_pswd)

    # TestIdx: 7-17. Parameters is same to `test_verify_pswd.py`
    # [New password] Invalid
    class TestChangePsswdInvalidNewPaswd(object):
        def test_change_pswd_not_enough_length(self):
            old_pswd = pswd_generator()
            new_pswd = pswd_changer(old_pswd)[:-1]
            assert not change_pswd(old_pswd, new_pswd)

        def test_change_pswd_over_valid_length(self):
            old_pswd = pswd_generator(length=MAX_VALID_LENGTH)
            new_pswd = pswd_changer(old_pswd) + 'A'
            assert not change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('invalid_char', ['-', 'あ', '^', '朝', 'ไทย', 'Ａ'])  # Ａ is full-width
        def test_change_pswd_various_invalid_char(self, invalid_char):
            old_pswd = pswd_generator()
            new_pswd = pswd_changer(old_pswd)[:-1] + invalid_char
            assert not change_pswd(old_pswd, new_pswd)

        def test_change_pswd_no_special_char(self):
            old_pswd = pswd_generator()
            new_pswd = pswd_changer(pswd_generator(incl_sp_char=False))
            assert not change_pswd(old_pswd, new_pswd)

        def test_change_pswd_no_upper_char(self):
            old_pswd = pswd_generator()
            new_pswd = pswd_generator(incl_upper_char=False)
            assert not change_pswd(old_pswd, new_pswd)

        def test_change_pswd_no_lower_char(self):
            old_pswd = pswd_generator()
            new_pswd = pswd_generator(incl_lower_char=False)
            assert not change_pswd(old_pswd, new_pswd)

        def test_change_pswd_no_numeric_char(self):
            old_pswd = pswd_generator()
            new_pswd = pswd_generator(incl_num=False)
            assert not change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM + 1])
        def test_change_pswd_over_continuous_same_char_num(self, continous_num):
            old_pswd = pswd_generator()
            new_pswd = pswd_generator(pswd_base='a'*continous_num)
            assert not change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('length', [21])  # [odd] num:11, alphabet:9, sp:1
        def test_change_pswd_num_more_than_half_of_length_odd(self, length):
            old_pswd = pswd_generator()
            new_pwsd = pswd_generator(pswd_base='!123', length=length, incl_sp_char=False)
            assert not change_pswd(old_pswd, new_pwsd)

        @pytest.mark.parametrize('length', [20])  # [even] num:11, alphabet:8, sp:1
        def test_change_pswd_num_more_than_half_of_length_even(self, length):
            old_pswd = pswd_generator()
            new_pswd = pswd_generator(pswd_base='!123', length=length, incl_sp_char=False)
            assert not change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('sp_char_num', [MAX_SP_CHAR_NUM+1])
        def test_change_pswd_over_sp_char_num(self, sp_char_num):
            old_pswd = pswd_generator()
            pswd = ''.join([SP_CHARS[i % len(SP_CHARS)] for i in range(sp_char_num)])
            new_pswd = pswd_generator(pswd_base=pswd, incl_sp_char=False)
            assert not change_pswd(old_pswd, new_pswd)

    # TestIdx: 18-22. Parameters is same to `test_verify_pswd.py`
    # [New password] Valid
    class TestChangePsswdValidNewPaswd(object):

        @pytest.mark.parametrize('length', [MIN_VALID_LENGTH, MIN_VALID_LENGTH + 1])
        def test_change_pswd_valid_length_less_than_100(self, length):
            old_pswd = pswd_generator(length=length)
            new_pswd = pswd_changer(old_pswd, diff_ratio=0.3)
            assert change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('length', [MAX_VALID_LENGTH])
        def test_change_pswd_valid_length(self, length):
            old_pswd = pswd_generator(length=length)
            new_pswd = pswd_changer(old_pswd)
            assert change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('continous_num', [MAX_CHAR_CONTINUOUS_NUM-1, MAX_CHAR_CONTINUOUS_NUM])
        def test_change_pswd_valid_continuous_same_char_num(self, continous_num):
            old_pswd = pswd_generator(pswd_base='a' * continous_num, length=100)
            new_pswd = pswd_changer(old_pswd)
            assert change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('length', [21])  # [odd] num:10, alphabet:10, sp:1
        def test_change_pswd_num_less_than_half_of_length_odd(self, length):
            old_pswd = pswd_generator(pswd_base='!12', length=length, incl_sp_char=False)
            new_pswd = pswd_changer(old_pswd, diff_ratio=0.3)
            assert change_pswd(old_pswd, new_pswd)

        @pytest.mark.parametrize('length', [20])  # [even] num:9, alphabet:10, sp:1
        def test_change_pswd_num_less_than_half_of_length_even(self, length):
            old_pswd = pswd_generator(pswd_base='!1', length=length, incl_sp_char=False)
            new_pswd = pswd_changer(old_pswd, diff_ratio=0.3)
            assert change_pswd(old_pswd, new_pswd)

    # TestIdx: 23
    # [Old password] Doesn't exist in the system
    def test_change_pswd_not_found(self):
        old_pswd = load_system_pswd()[-1]*2
        new_pswd = 'DUMMY'
        assert not change_pswd(old_pswd, new_pswd)
