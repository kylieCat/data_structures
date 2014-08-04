import pytest
from parens import proper_parens2


tests = {
    u')(': -1,
    u'((((()))))': 0,
    u'()()()()()()': 0,
    u'(((()))': 1,
    u'(((()))))': -1,
    u'()(()())': 0,
    u'(()(((()))))': 0,
    u'(((())))(()))': -1,
    u'()(())((()))(((()))': 1,
    u'': 0,
    u'(' * 1000000: 1
}


def test_proper_parens2():
    for test in tests:
        assert proper_parens2(test) == tests[test]
