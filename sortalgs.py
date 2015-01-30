import heapq


def bubble_sort(items):
    """Implementation of bubble sort.

    Time complexity: O(n**2)
    """
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j+1], items[j]


def insertion_sort(items):
    """Implementation of insertion sort.

    Time complexity: O(n**2)
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1


def selection_sort(items):
    """Implementation of selection sort.

    Time complexity: O(n**2)
    """
    for i in reversed(range(len(items))):
        # Find the index of greatest item in items[:i+1].
        greatest = 0
        for j in range(1, i + 1):
            if items[j] > items[greatest]:
                greatest = j
        items[i], items[greatest] = items[greatest], items[i]


def merge_sort(items):
    """Implementation of mergesort.

    Time complexity: O(n*log(n))
    """
    if len(items) > 1:

        mid = len(items) // 2        # Determine the midpoint and split
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)            # Sort left list in-place
        merge_sort(right)           # Sort right list in-place

        l, r = 0, 0
        for i in range(len(items)):     # Merging the left and right list

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')


def quick_sort(items):
    """Implementation of quick sort.

    Time complexity: O(n*log(n))
    """
    if len(items) > 1:
        pivot_index = len(items) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items


def heap_sort(items):
    """Implementation of heap sort.

    Time complexity: O(n*log(n))
    """
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for _ in range(len(items))]


def radix_sort(items, base=10):
    """Implementation of radix sort.

    Time complexity: O(kn)
    k - length of the longest number
    """
    maxval = max(items)
    for x in range(len(str(maxval))):
        bins = [[] for _ in range(base)]
        for y in items:
            bins[(y // 10**x) % base].append(y)
        items[:] = [item for section in bins for item in section]
