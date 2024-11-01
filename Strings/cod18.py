"""
26- Given 2 strings, a and b, return a new string made of the first char of a and the last char of b. If either string is length 0, use ‘@’ for its missing char.

Ex. (“last”, “chars”) → “ls”
Ex. (“yo”, “java”) → “ya”

"""


def combineStrings(str1, str2):
    resutltString = ""
    if len(str1) == 0:
        charFirst = "@"
    else:
        charFirst = str1[0]
    if len(str2) == 0:
        charLast = "@"
    else:
        charLast = str2[-1]
    resultString = charFirst + charLast
    return resultString

print(combineStrings("", "chars"))