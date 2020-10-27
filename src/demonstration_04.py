"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length: int, width: int) -> int:
    # Your code here
    # take length and width ints, treat them as dimensions
    # of an imaginary rectange
    # perimiter = length * 2 + width * 2
    perimiter = length * 2 + width * 2
    # return the perimiter of imaginary rectangle
    return perimiter

print(find_perimeter(6, 7))

