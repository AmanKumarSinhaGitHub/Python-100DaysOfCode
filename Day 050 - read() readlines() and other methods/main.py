import os

os.chdir("Day 050 - read() readlines() and other methods")





# READ LINES #

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()





# Program to read students marks for marks.txt file
f = open('marks.txt', 'r')
i = 0
while True:
    i=i+1
    line = f.readline()
    
    if not line:
        break
    print(line)

    # Split the line into individual subject marks
    marks_list = line.split(',')
    maths = int(marks_list[0])
    english = int(marks_list[1])
    science = int(marks_list[2])

    print(f"Student No. {i} marks in Maths = {maths}")
    print(f"Student No. {i} marks in English = {english}")
    print(f"Student No. {i} marks in Science = {science}")

f.close()

    
# WRITE LINES
f = open('myfile2.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()