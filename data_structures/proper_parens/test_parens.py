from data_structures.proper_parens.parens import proper_parens2


tests = {
    ')(': -1,
    '((((()))))': 0,
    '()()()()()()': 0,
    '(((()))': 1,
    '(((()))))': -1,
    '()(()())': 0,
    '(()(((()))))': 0,
    '(((())))(()))': -1,
    '()(())((()))(((()))': 1,
    '': 0,
    '(' * 1000000: 1
}


def test_proper_parens2():
    for test in tests:
        assert proper_parens2(test) == tests[test]
