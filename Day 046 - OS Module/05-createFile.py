import os

# change the current directory to "new-folder"
os.chdir("Day 046 - OS Module/new-folder")

# create a new file named "file.txt" in "new-folder"
for i in range(0,10):
    os.chdir(f"Tutorial {i+1}")

    f = open("file.txt", "w")
    # Write "Hello" inside everyfile file
    f.write("Hello")
    f.close()
    
    # command to go up one level from the current directory
    os.chdir("..")



    