def insertion(lst):
    if not lst or len(lst) < 2:
        return lst
    for idx, _ in enumerate(lst):
        while idx > 0 and lst[idx-1] > lst[idx]:
            lst[idx], lst[idx-1] = lst[idx-1], lst[idx-1]
            idx -= 1



def merge(lst):
    if not lst or len(lst) < 2:
        return lst
    left, right = lst[:len(lst) >> 1], lst[len(lst) >> 1:]
    left = merge(left)
    right = merge(right)
    return _merge(left, right)


# function merge(left, right)
#     var list result
#     // assign the element of the sublists to 'result' variable until there is no element to merge.
#     while length(left) > 0 or length(right) > 0
#         if length(left) > 0 and length(right) > 0
#            // compare the first two element, which is the small one, of each two sublists.
#             if first(left) <= first(right)
#                 append first(left) to result
#                 left = rest(left)
#             else
#                 append first(right) to result
#                 right = rest(right)
#         else if length(left) > 0
#             append first(left) to result
#             left = rest(left)
#         else if length(right) > 0
#             append first(right) to result
#             right = rest(right)
#     end while
#     return result
def _merge(left, right):
    result = []
    while len(left) and len(right):
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
