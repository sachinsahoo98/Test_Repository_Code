import re

string1 = "sachin.s.sahoo@gmail.com.spc"
string2 = "Rohit32198729$"
string3 = "zyax, xyaaz, zyyax, zaaayx, xyyyyza"

match1 = re.search(r'\.', string1)
match2 = re.search(r'[@]', string1)
print(match1, match2)
match3 = re.search(pattern=r'^R', string=string2)
match4 = re.search(r'\$', string2)
match5 = re.findall(r's.c', string1)
match6 = re.findall(r"sac|soc", string1)
match7 = re.findall(r"zy?", string3)
match8 = re.findall(r"zy+", string3)
match9 = re.findall(r'za*', string3)
match10 = re.findall(r"a{2,3}", string3)
match11 = re.findall(r'(z|x)y{2}', string3)
print(match7, match8, match9, match10, match11)
print(match3, match4, match5)
print(match6)