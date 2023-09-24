import os

os.chdir("Day 075 - Solution Clear the Clutter")


files = os.listdir('my-clutter-folder')

i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f'my-clutter-folder/{file}', f'my-clutter-folder/{i}.png')
        i+=1