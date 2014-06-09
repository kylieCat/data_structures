__author__ = 'eyuelabebe'

def _proper_parent(_file):

    matching_parenthesis = {'{': '}', '(': ')', '[': ']'}
    all_parenthesis = ['{', '}', '(', ')', '[', ']']

    collection = []
    open_parenthesis = []
    closed_parenthesis = []

    _stop = False

    with open(_file, 'r') as test_file:
        while not _stop:
            file = list(test_file.read())

            if not file:
                _stop = True

            for letter in file:
                if letter in all_parenthesis:
                    collection.append(letter)

            if len(collection) % 2 == 0:
                count = 0
                _full = len(collection)
                _iter = len(collection) / 2

                for i in range(_iter):
                    if matching_parenthesis[collection[_iter - 1 - i]] == collection[_iter + i]:
                        count += 1
                    else:
                        return -1
                return 1
            else:

                for i in collection:
                    if i in matching_parenthesis.keys():
                        open_parenthesis.append(i)
                    else:
                        closed_parenthesis.append(i)

                if len(open_parenthesis) == len(closed_parenthesis):
                    result = 0
                    _stop = True
                else:
                    if (len(open_parenthesis) > len(closed_parenthesis)):
                        result = 1
                    else:
                        result = -1
                _stop = True

    return result

