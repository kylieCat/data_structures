def proper_parens(parens):
    """
    Takes a unicode string of parenthesis and checks to see if it is balanced.
    Returns:
    1: String is open, too many '('
    0: String is balanced
    -1: String is broken, too many ')'
        >>> proper_parens(')(')
        -1
        >>> proper_parens('(())')
        0
        >>> proper_parens('(()')
        1
    """
    valid_chars = {'(': 1, ')': -1}
    count = sum(valid_chars.get(p, 0) for p in parens)
    return int(bool(count)) if count >= 0 else -1


def proper_parens2(parens):
    """
    Takes a string of parenthesis and checks to see if it is balanced.
    Returns:
    1: String is open, too many '('
    0: String is balanced
    -1: String is broken, too many ')'

        >>> proper_parens(')(')
        -1
        >>> proper_parens('(())')
        0
        >>> proper_parens('(()')
        1
        >>> proper_parens('(hello)')
        0
    """
    total = 0
    valid_chars = {'(': 1, ')': -1}
    for paren in parens:
        total += valid_chars.get(paren, 0)
        if total < 0:
            return -1
    return int(bool(total))
