"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt: str) -> bool:
    # Your code here
    # lets keep 2 vars, one for x's one for o's
    xs = 0
    os = 0


    # figure out # of o's and x's in input string
    # wee need to check every char in the txt, so iterate over txt
    # check for case insensitivity
    # either like below or with string.lower
    for character in txt:
        # if we see an x: increment xs
        if character == "x" or character == "X":
            xs += 1
        # if we see an o: increment os
        if character == "o" or character == "O":
            os += 1

    # check if # of each is the same
    # if xs == os:
    #     return True
    # else :
    #     return False
    #   but this is messy & computationally harder
    # return true if they are, false otherwise
    return xs == os


print(XO("ooxx")) # ➞ True
print(XO("xooxx"))# ➞ False
print(XO("ooxXm"))# ➞ True (Case insensitive)
print(XO("zpzpzpp"))# ➞ True (Returns True if no x and o)
print(XO("zzoo"))# ➞ False