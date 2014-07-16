def insertion(lst):
    if not lst or len(lst) < 2:
        return lst
    for idx, _ in enumerate(lst):
        while idx > 0 and lst[idx-1] > lst[idx]:
            lst[idx], lst[idx-1] = lst[idx-1], lst[idx]
            idx -= 1


def merge(lst):
    if not lst or len(lst) < 2:
        return lst
    left, right = lst[:len(lst) >> 1], lst[len(lst) >> 1:]
    left = merge(left)
    right = merge(right)
    return _merge(left, right)


def _merge(left, right):
    result = []
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left):
            result.append(left[0])
            left = left[1:]
        elif len(right):
            result.append(right[0])
            right = right[1:]
    return result


def quick(lst, i=0, k=len(lst)):
    if i < k:
        p = partition(lst, i, k)
        quick(lst, i, p-1)
        quick(lst, p + 1, k)