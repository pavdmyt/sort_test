import timeit


# bubble sort:
setup_bub = '''
import random
from sortalgs import bubble_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = bubble_sort
'''

# insertion sort:
setup_ins = '''
import random
from sortalgs import insertion_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = insertion_sort
'''

# selection sort:
setup_sel = '''
import random
from sortalgs import selection_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = selection_sort
'''

# merge sort:
setup_mer = '''
import random
from sortalgs import merge_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = merge_sort
'''

# quick sort:
setup_qui = '''
import random
from sortalgs import quick_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = quick_sort
'''

# heap sort:
setup_hea = '''
import random
from sortalgs import heap_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = heap_sort
'''

# radix sort:
setup_rad = '''
import random
from sortalgs import radix_sort

random.seed('eggs')
s = [random.randrange(10**6) for x in range(1000)]
sort = radix_sort
'''

# Actual test:
for setup in [setup_bub, setup_ins, setup_sel, setup_mer, setup_qui,
              setup_hea, setup_rad]:
    print(setup.split()[-1])
    print(min(timeit.Timer('a=s[:]; sort(a)', setup=setup).repeat(7, 100)))
    print('')
