"""
To Create strings in python, one can use a str() method or basically wrap the characters within single or double quotes.

Defination:
Strings:- It is an ordered sequence of characters, meaning elements of the strings can accessed using its indices.
Strings are immutable in nature, meaning once they are defined/created, the value it cannot be changed.
The attempt to modify strings only creates new strings without modifying original ones.

"""
#converting any data type to string type
a = str()
#to create empty string
cstr = ""

#to create a string using a sequence of characters
detail = "Hi this is sachin sourav sahoo"

#print the string
print("The string is:", detail)

#to access elements of the string using indices
print("First Element",detail[0])
print("Last Element", detail[-1]) #using negative index

#to find the length of the string
print("Length of string is", len(detail))

#to traverse a string using for Loop
print("Traversed String is:")
for char in detail:
    print(char, end="")

#slicing of the string
"""
Process to extract part of the string
"""
#stringname[startIndex:endIndex:stepValue]
"""
Starting and Ending index can be optional, Step value is default 1 if not specified
"""
print("\n")
print(detail[0:]) #End index is optional, default step value 1
print(detail[:3:2])#Start index is optional, with ending index upto 3 but not included 3, with step value 2
print(detail[::-1]) #Reverse a string, special operation

#trying to access a string index not available will lead to IndexError, string index out of range
#print(detail[31])


"""
String Literals:
Sequence of characters enclosed within "" or ''
Ex: 
firstName = 'sachin'
lastName = 'sahoo'
middleName = "sourav"
"""
firstName = 'sachin'
lastName = 'sahoo'
middleName = "sourav"

print(firstName, middleName, lastName)

#Escape Sequences in Strings.
"""
It is achieved using  blackslash '\' operator in a string.
Example:-
"""
str = 'Hi it\'s sachin'
print(str)

"""
Different Escape Sequences:-
\t : for tab space
\n : for newline 
\r : for carriage return
"""
#Examples:

greet = ('Hello\
         World\
         ')
print(greet)
