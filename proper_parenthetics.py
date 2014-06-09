__author__ = 'eyuelabebe'

def _proper_parent():

    matching_parenthesis = {'{': '}', '(': ')', '[': ']'}
    all_parenthesis = ['{', '}', '(', ')', '[', ']']

    collection = []
    open_parenthesis = []
    closed_parenthesis = []

    _stop = False

    with open('test.txt', 'r') as test_file:
        while not _stop:
            file = list(test_file.read())

            if not file:
                _stop = True

            for letter in file:
                if letter in all_parenthesis:
                    collection.append(letter)

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

    return  result


