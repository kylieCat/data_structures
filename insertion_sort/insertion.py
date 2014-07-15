def insertion_sort(lst):
    if not lst or len(lst) < 2:
        return lst
    for idx, _ in enumerate(lst):
        while idx > 0 and lst[idx-1] > lst[idx]:
            lst[idx], lst[idx-1] = lst[idx-1], lst[idx-1]
            idx -= 1