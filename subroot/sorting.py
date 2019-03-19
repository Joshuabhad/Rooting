def bubble_sort(items):

    """
    compares adjacent items and exchanges those that are out of order

    items: list input to be sorted

    returns: array of items sorted in ascending order

    example: bubble_sort([3,1,12,2,5,4])
    >>>[1, 2, 3, 4, 5, 12]

    """

    for i in range(len(items)-1):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return(items)


def merge_sort(items):

    """
    Divide two halves of a list, sort and then merge together

    (items): list to be sorted

    returns: list array of items sorted in ascending order

    Example: merge_sort([36,1,12,26,26,14])
    >>>[1, 12, 14, 26, 26, 36]

    """

    if len(items) > 1:
        left, right = map(lambda l: list(reversed(merge_sort(l))), (items[::2], items[1::2]))
        items.clear()
        while left and right:
            items.append(left.pop() if left[-1] < right[-1] else right.pop())
        items.extend(left[::-1])
        items.extend(right[::-1])
    return items


def quick_sort(items):

    """
    Sort items in an array

    items: list input

    returns: list array of items sorted in ascending order

    Example: quick_sort([36,1111,2222,26,226,14])
    >>>[14, 26, 36, 226, 1111, 2222]

    """

    if len(items) == 0:
        return items
    pivot = items[0]
    b = [x for x in items if x == pivot]
    small = quick_sort([x for x in items if x < pivot])
    large = quick_sort([x for x in items if x > pivot])
    return small + b + large
