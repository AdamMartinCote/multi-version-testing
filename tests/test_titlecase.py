# -*- coding: utf-8 -*-
import sys

import pytest
from hypothesis import given, strategies, assume
from pytest import mark

from titlecase import title_case


class TestTitleCase:
    @mark.smoke
    @given(string=strategies.text())
    @pytest.mark.skipif(
        sys.version_info[0] == 2,
        reason="String literals are of type unicode in Python2.7"
    )
    def test_should_return_a_string(self, string):
        s = title_case(string)
        assert type(s) == str

    @given(string=strategies.text())
    @pytest.mark.skipif(
        sys.version_info[0] == 2,
        reason="String literals are of type unicode in Python2.7"
    )
    def test_should_not_increase_string_size(self, string):
        assume("ß" not in string)  # Capitalization of this character is 2 characters
        s = title_case(string)
        assert len(s) == len(string)

    @given(string=strategies.text(min_size=1))
    def test_should_capitalize_the_first_letter(self, string):
        s = title_case(string)
        assert s[0] == s[0].upper()

    def test_should_capitalize_words_which_are_not_exceptions(self):
        string = "this should be all capitalized alright"
        got = title_case(string)
        expected = "This Should Be All Capitalized Alright"
        assert got == expected
