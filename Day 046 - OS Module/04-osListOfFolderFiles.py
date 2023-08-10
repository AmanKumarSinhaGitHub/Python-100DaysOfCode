import os

os.chdir("Day 046 - OS Module")

folders = os.listdir("new-folder")
# Show all folders
for i in folders:
    print(i)