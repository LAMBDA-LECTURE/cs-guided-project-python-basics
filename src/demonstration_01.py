"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""
def addition(a: int, b: int):
    # what happens if we input striubg instead
    # given 2 ints as inputs
    # add the 2 inputs toget with +
    answer = a + b
    # return the result of the operation to make the result available outside this fn
    return answer

    # streamlined
    # return a + b

addition(3, 2)

