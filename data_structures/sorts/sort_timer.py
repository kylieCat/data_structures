import timeit


setup = """
from random import randint
import sorts
insertion = sorts.insertion
merge = sorts.merge
quick = sorts.quick


"""
ten_thousand = 'lst = [randint(1,1000) for _ in range(10000)]'
hundred_thousand = 'lst = [randint(1,1000) for _ in range(100000)]'
million = 'lst = [randint(1,1000) for _ in range(1000000)]'

# Insertion Sort timing
print('Starting insertion sort 10,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; insertion(lst)',
        setup=setup+ten_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))
print('Starting insertion sort 100,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; insertion(lst)',
        setup=setup+hundred_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))

# Merge Sort timing
print('Staring merge sort 10,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; merge(lst)',
        setup=setup+ten_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))
print('Starting merge sort 100,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; merge(lst)',
        setup=setup+hundred_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))

# Quick Sort timing
print('Starting quick sort 10,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; quick(lst)',
        setup=setup+ten_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))
print('Starting quick sort 100,000 elements')
m = min(
    timeit.Timer(
        'l = lst[:]; quick(lst)',
        setup=setup+hundred_thousand).repeat(1, 2)
)
print('Minimum time: {}'.format(m))
