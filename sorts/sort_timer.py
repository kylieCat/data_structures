setup = """
from random import randint
import sorts
insertion = sorts.insertion
merge = sorts.merge
quick = sorts.quick
"""
ten_thousand = 'lst = [randint(1,1000) for _ in range(10000)'
hundred_thousand = 'lst = [randint(1,1000) for _ in range(100000)'
million = 'lst = [randint(1,1000) for _ in range(1000000)'

print('Staring insertion sort 10,000 elements')