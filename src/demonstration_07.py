"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
from typing import List

def nth_smallest(lst: List[int], n: int) -> int:
    # Your code here
    # what if there is no nth smallest?
    # check if n > len(lst) to determine if there is an nth smallese
    if n > len(lst):
        return None
    else:
        # given an usorted array, find the n'th smallest
        # note that the smallest element is the first smallest
        # sort the list by size
        lst.sort()
        # then fetch the nth item
        # remembering to use n-1
        n_smallest = lst[n - 1]
        # return the nth smallest number
        return n_smallest

print(nth_smallest([7, 5, 3, 1], 1))# ➞ 1
print(nth_smallest([1, 3, 5, 7], 3))# ➞ 5
print(nth_smallest([1, 3, 5, 7], 5))# ➞ None
print(nth_smallest([7, 3, 5, 1], 2))# ➞ 3