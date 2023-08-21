import os
os.chdir("Day 051 - seek(), tell() and other functions")





# Note : file.txt = Hey, I am learning Python Programming Language
with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # .tell()
  print(f.tell()) # 10

  # Read the next 5 bytes
  data = f.read(5)
  print(data)







with open('sample.txt', 'w') as f:
  f.write("Hello World!")
  f.truncate(5)
  # Now dample.txt = "Hello"