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
    place = _max_digits(lst)
    result = lst[:]
    for i in xrange(place):
        result = _flatten(_split(lst, i))
        print(result)
    return result


def _radify(number, place):
    return number // 10 ** place % 10


def _make_buckets():
    return [[] for _ in xrange(10)]


def _max_digits(lst):
    max_num = max([abs(num) for num in lst])
    places = 0
    while max_num:
        max_num /= 10
        places += 1
    return places


def _split(lst, place):
    buckets = _make_buckets()
    for num in lst:
        buckets[_radify(num, place)].append(num)
    return buckets


def _flatten(lst):
    flat = []
    for sub in lst:
        flat.extend(sub)
    return flat