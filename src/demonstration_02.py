"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes: int) -> int:
    # Your code here
    # we know there are 60 seconds in a minute
    # we need to take "minutes" and multiply by 60
    # in order to perforn the conversion
    seconds = minutes * 60
    # return the converted result
    return seconds

    #return minutes * 60
print(convert(5))