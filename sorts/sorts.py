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


def quick(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    l = quick([x for x in lst[1:] if x < pivot])
    u = quick([x for x in lst[1:] if x >= pivot])
    return l + [pivot] + u


def radix(lst):
    rad_lst = _radify(lst)
    buckets = _make_buckets()
    place = _max_abs(lst)
    result = []
    for i in xrange(place):
        for num in rad_lst:
            buckets[num[-1 - i]].append(num)
        result.extend(buckets)
    return result


def _radify(lst):
    result = []
    passes = _max_abs(lst)
    for element in lst:
        rad = []
        for i in xrange(passes):
            rad[0:0] = element % 10,
            element /= 10
        result.append(tuple(rad))
    return result


def _make_buckets():
    return [[] for _ in xrange(10)]


def _max_abs(lst):
    max_num = max([abs(num) for num in lst])
    places = 0
    while max_num:
        max_num /= 10
        places += 1
    return places