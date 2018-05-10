from unittest.mock import Mock
from nscollector import gatherers


def test_strip_word():
    bs_obj = Mock(getText=Mock(side_effect=['Test1: foo', 'Test2: foo']))
    assert gatherers._strip_word(bs_obj, 'Test1: ') == 'foo'
    assert gatherers._strip_word(bs_obj, 'Test1: ') == 'Test2: foo'
