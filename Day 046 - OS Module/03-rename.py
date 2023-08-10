import os
os.chdir("Day 046 - OS Module")

# Rename every file, Replace Day with Tutorial
for i in range(0, 10):
    os.rename(f"new-folder/Day {i+1}", f"new-folder/Tutorial {i+1}")