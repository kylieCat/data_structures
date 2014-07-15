def insertion(lst):
    if not lst or len(lst) < 2:
        return lst
    for idx, _ in enumerate(lst):
        while idx > 0 and lst[idx-1] > lst[idx]:
            lst[idx], lst[idx-1] = lst[idx-1], lst[idx]
            idx -= 1


# function merge_sort(list m)
#     // Base case. A list of zero or one elements is sorted, by definition.
#     if length(m) <= 1
#         return m
#
#     // Recursive case. First, *divide* the list into equal-sized sublists.
#     var list left, right
#     var integer middle = length(m) / 2
#     for each x in m before middle
#          add x to left
#     for each x in m after or equal middle
#          add x to right
#
#     // Recursively sort both sublists.
#     left = merge_sort(left)
#     right = merge_sort(right)
#     // *Conquer*: merge the now-sorted sublists.
#     return merge(left, right)

def merge(lst):
    if not lst or len(lst) < 2:
        return lst
