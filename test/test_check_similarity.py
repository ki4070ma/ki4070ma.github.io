#!/usr/bin/env python

from test.helper.helper import (
    strings_generator_dest_str_longer,
    strings_generator_matched_char_mixed,
    strings_generator_same_center,
    strings_generator_same_head,
    strings_generator_same_tail,
    strings_generator_src_string_longer
)

import pytest  # type: ignore

from change_pswd_func.check_similarity import similar


class TestCheckSimilarity(object):

    def test_similar_exception(self):
        with pytest.raises(TypeError):
            similar(123, [1, 2, 3])

    class TestCheckSimilaritySameLengthMatchTailString(object):
        '''
        Case:
            str1: XXXooooooo
            str2: oooooooooo
        '''

        # TestIdx: 1, 2
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_similar_dissimilar(self, str_diff_num):
            str1, str2 = strings_generator_same_tail(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 3
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_similar_similar(self, str_diff_num):
            str1, str2 = strings_generator_same_tail(str_diff_num)
            assert similar(str1, str2)

    class TestCheckSimilaritySameLengthMatchCenterString(object):
        '''
        Case:
            str1: ooooXXXooo
            str2: oooooooooo
        '''

        # TestIdx: 4, 5
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_similar_dissimilar(self, str_diff_num):
            str1, str2 = strings_generator_same_center(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 6
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_similar_similar(self, str_diff_num):
            str1, str2 = strings_generator_same_center(str_diff_num)
            assert similar(str1, str2)

    class TestCheckSimilaritySameLengthMatchHeadString(object):
        '''
        Case:
            str1: oooooooXXX
            str2: oooooooooo
        '''

        # TestIdx: 7, 8
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_similar_dissimilar(self, str_diff_num):
            str1, str2 = strings_generator_same_head(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 9
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_similar_similar(self, str_diff_num):
            str1, str2 = strings_generator_same_head(str_diff_num)
            assert similar(str1, str2)

    class TestCheckSimilaritySameLengthMixedMatchStrings(object):
        '''
        Case:
            str1: oXoXoXoooo
            str2: oooooooooo
        '''

        # TestIdx: 10, 11
        @pytest.mark.parametrize('str_diff_num', [-1, 0])  # 79%/80% matching
        def test_similar_dissimilar(self, str_diff_num):
            str1, str2 = strings_generator_matched_char_mixed(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 12
        @pytest.mark.parametrize('str_diff_num', [1])  # 81% matching
        def test_similar_similar(self, str_diff_num):
            str1, str2 = strings_generator_matched_char_mixed(str_diff_num)
            assert similar(str1, str2)

    class TestCheckSimilarityDifferentStringLength(object):
        '''
        Case1:
            str1: ooooooo
            str2: oooooooooo
        '''

        # TestIdx: 13, 14
        @pytest.mark.parametrize('str_diff_num', [-1, 0])
        def test_similar_dissimilar_dest_string_longer(self, str_diff_num):  # 79%/80% matching
            str1, str2 = strings_generator_dest_str_longer(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 15
        @pytest.mark.parametrize('str_diff_num', [1])
        def test_similar_similar_dest_string_longer(self, str_diff_num):  # 81% matching
            str1, str2 = strings_generator_dest_str_longer(str_diff_num)
            assert similar(str1, str2)

        '''
        Case2:
            str1: oooooooooo
            str2: ooooooo
        '''
        # TestIdx: 16, 17
        @pytest.mark.parametrize('str_diff_num', [-1, 0])
        def test_similar_dissimilar_src_string_longer(self, str_diff_num):  # 79%/80% matching
            str1, str2 = strings_generator_src_string_longer(str_diff_num)
            assert not similar(str1, str2)

        # TestIdx: 18
        @pytest.mark.parametrize('str_diff_num', [1])
        def test_similar_similar_src_string_longer(self, str_diff_num):  # 81% matching
            str1, str2 = strings_generator_src_string_longer(str_diff_num)
            assert similar(str1, str2)
