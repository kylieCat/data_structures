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
    try:
        valid_chars = {'(': 1, ')': -1}
        count = sum((
            valid_chars[p] if p in valid_chars else str(p) for p in parens
        ))
        return int(bool(count)) if count >= 0 else -1
    except TypeError:
        print('Invalid character in string')
        raise ValueError()


def proper_parens2(parens):
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
    total = 0
    valid_chars = {'(': 1, ')': -1}
    for paren in parens:
        total += valid_chars[paren]
        if total < 0:
            return -1
    return int(bool(total))