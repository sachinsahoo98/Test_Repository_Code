"""
Write a  Python function that takes a list of words and return the longest word and the length of the longest one.

inplist = ["sachin", "sourav", "sahoo"]

"""

def retrieveLongestWord(inpList):
    outstring = ""
    maxstrLen = 0

    for word in inpList:
        if len(word) > maxstrLen:
            maxstrLen = len(word)
            outstring = word
    return (outstring, maxstrLen)

print(retrieveLongestWord(["sachin", "ajay", "sandhya"]))