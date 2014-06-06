def proper_parens(parens):
    """
    
    Takes a unicode string of parenthesis and checks to see if it is balanced.
    
    Returns:
    1 - String is open, too many (
    0 - String is balanced
    -1 - String is broken, too many )
    
    """
    try:
        valid_chars = {u'(' : 1, u')' : -1}
        count = sum((valid_chars[paren] if paren in valid_chars else paren for paren in parens))
        return int(bool(count)) if count >= 0 else -1
    except TypeError:
        print ('Invalid character in string')
        raise ValueError()