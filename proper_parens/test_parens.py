import pytest
from proper_parens import proper_parens


tests = {
    u')('
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
    with pytest.raises(ValueError):
        proper_parens('r')
    for test in tests:
        assert proper_parens(test) == tests[test]