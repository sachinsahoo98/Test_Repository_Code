import re

string1 = "xyqa, xyyaz, xyyypopaz, yxaaaop, yzaaapk, yxpal"
string2 = "sachin.s.sahoo@gmail.com"
string3 = "test$)(*&^%$#@!"


#matches the character class
match1 = re.search(r'[$)]', string3)
print(match1)

#matches the start of the string
match2 = re.findall(r'^x', string1)
print(match2)

#matches the end of the string
match3 = re.findall(r'p$', string1)
print(match3)

#matches any char in between the string except newline
match4 = re.findall(r'x.yy', string1)
print(match4)

#matches zero or one instances in string
match5 = re.findall(r'xy?', string1)
print(match5)

#matches one or more instance in string
match6 = re.findall(r'xy+', string1)
print(match6)

#matches any instances of the specified char
match7 = re.findall(r'xy*', string1)
print(match7)

# matches either the pattern in right or left of or operator available
match8 = re.findall(r'x.yy|x.p', string1)
print(match8)

match9 = re.findall(r'[x|y]x', string1)
print(match9)

#to check if the string is starting with a given character. r\A{string or char}

match10 = re.findall(r'\As', string2)
print(match10)

#to check if the string is starting with given char or ending with given char

match11 = re.findall(r'com\b', string2)
match12 = re.findall(r'\bsachin', string2)
print(match11, match12)

#\B is opposite to \b. string should not start with \b or end with \b

match13 = re.findall(r'sac\B', string2)
match14 = re.findall(r'\Bgmail', string2)
print(match13, match14)