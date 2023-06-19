# Length of a string : len()
a = "Coding"
print("The Length of word \"" + a + "\" is" ,len(a));
# Output : The Length of word "Coding" is 6


# UPPER CASE : upper()
print(a.upper())
# Output : CODING


# lower case : lower()
print(a.lower())
# Output : lower


#  Remove trailing characters from the right end of a string. 
# "Trailing characters" refer to any characters located at the end of the string.
b = "Aman Kumar Sinha!!!!!!!!!!!!!!!!!!!!"
print(b.rstrip("!"))
# Output : Aman Kumar Sinha


# Replace all occurrences of a substring with a new substring
string = "Hello, World!"
print(string.replace("o", "e"))
# Output : Helle, Werld!


# Split a string into a list of substring based on a specified delimiter
str = "Hello@World@How@Are@You"
print(str.split("@"))
# Output : ['Hello', 'World', 'How', 'Are', 'You']


# Capatalized First letter of a work or sentense and rest to lower case
name = "aman KumaR"
print(name.capitalize())
# Output : Aman kumar


# Center a string within a specified width.
code = "python" 
print(code.center(30)) 
# Output :            python  
# Here, it take width of 30 char and print "python" in center


# Count the number of occuring of a substring in a string
d = "Python is a programming language. I am learning Python."
print(d.count("Python"))
# Output : 2


# Check whether a string ends with a specified suffix
x = "Hello  World"
print(x.endswith("World"))
# Output : True 


# Check whether a string starts with a specified prefix
x = "Hello  World"
print(x.startswith("World"))
# Output : False 


# Find the first occurrence of a substring within a string. 
str = "Hello World"
print(str.find("o"))
# Ouput : 4
print(str.find("g"))
# Output : -1
# It returns the index of the first occurrence of the substring if it is found, and -1 if the substring is not present in the string.


# The .index() method is a string method in Python that is used to find the index of the first occurrence of a substring within a string. 
# It is similar to the .find() method, but instead of returning -1 when the substring is not found, it raises a ValueError exception.
str = "Hello World"
print(str.index("o"))
# Ouput : 4
# print(str.index("g"))
# Output : ValueError: substring not found


# Checks whether all the characters in a string are alphanumeric (either letters or numbers). 
str = "Hello"
print(str.isalnum())
# Output : True
# It returns True if all the characters are alphanumeric, and False otherwise.


# Checks whether all the characters in a string are alphabetic (letters). 
str = "Hello6"
print(str.isalpha())
# Output : False
# It returns True if all the characters are letters, and False otherwise.


# Checks whether all the characters in a string are lowercase letters
str = "Hello"
print(str.islower())
# Output : False


# Checks whether all the characters in a string are uppercase letters
str = "HELLO"
print(str.isupper())
# Output : True


# Checks whether all the characters in a string are printable
string1 = "Hello"
print(string1.isprintable())  
# Output : True
string2 = "Hello\nWorld"
print(string2.isprintable())  
# Output : False


# Checks whether all the characters in a string are whitespace characters
string1 = "     "
print(string1.isspace()) 
# Output : True
string2 = "Hello  "
print(string2.isspace())  
# Output : False


# Checks whether a string follows the title case format.
string1 = "Hello World"
print(string1.istitle())  
# Output : True
string2 = "Hello world"
print(string2.istitle())  
# Output : False


# Convert to title case
string = "hello, world!"
print(string.title())
# Output : Hello, World!


# Uppercase characters to lowercase, and lowercase to uppercase.
string = "Hello, World!"
print(string.swapcase())
# Output : hELLO, wORLD!