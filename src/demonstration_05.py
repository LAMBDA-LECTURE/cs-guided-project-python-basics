"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # takes a list of strings and sorts them
    # so that shorter strings are first, with longest last
    # rephrase to google: how do we sort an array/list by length of elements
    # in python: '.sort' methon on lists sorts in-place
    # '.sort' defaults to sorting in alphabetical order, then length
    # we need  to tell .sort that we wanna sort by length instead
    lst.sort(key = len)
        # note: sorted is very much like .sort except it does return a new copy of your list, leaving the old list unchanged.
    # return sorted output
    return lst
print(sort_by_length(["a", "ccc", "xxxx", "dddd", "bb"]))
print(sort_by_length(["apple", "pie", "shortcake"]))
print(sort_by_length(["may", "april", "september", "august"]))
print(sort_by_length([]))


