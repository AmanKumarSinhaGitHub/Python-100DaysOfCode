import os
# change the current directory to "Day 049 - File IO"
os.chdir("Day 049 - File IO")





# READ MODE
f = open('myfile.txt', 'r')

text = f.read()
print(text) # Hello I am learning Python

f.close()

# Note : If you open a file in READ mode and it doesn't exist. It gives you error.
# But If you open a file in WRITE mode and it doesn't exist. It will create that file and not throw any error





# WRITE MODE
f = open('newFile.txt', 'w')
f.write('Hello, world!')

f = open('newFile.txt', 'r')
text = f.read()
print(text) # Hello, world!

f.close()





# APPEND
f = open('newFile.txt', 'a')
f.write(' I am Aman')

f = open('newFile.txt', 'r')
text = f.read()
print(text) # Hello, world! I am Aman

f.close()





# You can use the with statement to automatically close the file after you are done with it.
with open('newFile.txt', 'a') as f:
    f.write(" I am a coder")

# Now "newFile.txt" = Hello, world! I am Aman