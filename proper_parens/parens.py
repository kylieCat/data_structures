def proper_parens(parens):
    """
    Takes a unicode string of parenthesis and checks to see if it is balanced.
    Returns:
    1 - String is open, too many (
    0 - String is balanced
    -1 - String is broken, too many )
    """
    def check_braces(expressions):
        for expression in expressions:
            if _check_expression(expression):
                print(1)
            else:
                print(0)

    def _check_expression(expression):
        pairs = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in expression:
            if char in ['{', '(', '[']:
                stack.append(char)
            else:
                try:
                    if pairs[stack.pop()] == char:
                        continue
                    else:
                        raise IndexError
                except IndexError:
                    return False
        return True