"""
Python program to capitalize the first and last character of each word in a string

Input: hello world
Output: HellO WorlD
Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS

"""

"""
Approach 1:
Using Lists : split the strings using " " to retrieve words.
iterate over each word from the list.
find length of the word. if len==0 or len==n-1 and letter is lowercase, uppercase that Letter.
"""

def capitalizeTest(inpStr):
    wordsList = inpStr.split()
    captializedStr = ""

    for word in wordsList:
        sizeofWord = len(word)
        currIndex = 0
        for char in word:
            if (currIndex == 0 or currIndex== sizeofWord-1) and char.islower():
                captializedStr+= char.upper()
            else:
                captializedStr+= char
            currIndex+=1
        captializedStr += " "
    return captializedStr.strip()

out = capitalizeTest("hello world")
print(out)