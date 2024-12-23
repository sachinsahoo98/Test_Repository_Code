"""
Python | Program to accept the strings which contains all vowels.
"""

def checkStringAcceptance(paramString):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel = set()
    status = False
    for char in paramString:
        if char.lower() in vowels:
            vowel.add(char.lower())
    if vowel == vowels:
        status = True
    return status

def testAcceptance():
    assert checkStringAcceptance("namithai") == False
    assert checkStringAcceptance("sachinsouravsahooe") == True
