"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    # check to make sure that 'txt' makes sense as an int
    # the isnumeric fn checks if a string can be rep'd as a number
    if str.isnumeric(txt) is True:
    # if txt is a valid number
        #  inputs string and converts to integer
        # the 'int' fn does this for us in python
        # call the 'int' fn, passing in the 'txt' input
        converted_int = int(txt)
        # return the converted result
        return converted_int
        # return int(txt)
    # if txt is not a valid numer
    else:
        # return an error indicating that txt is not a valid number
        # use string interpolation to print out the actual value of 'txt'
        # use f-strings in python
        return f"'{txt}' is not a valid number"
print(string_int("1000"))
print(string_int("testing, testing"))
print("1000")