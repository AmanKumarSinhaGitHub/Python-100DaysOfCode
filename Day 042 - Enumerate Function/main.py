marks = [20, 90, 2, 5]

# Normal for loop
i = 0
for mark in marks:
    print(mark)
    if(i==1): 
        print("Great")
    i+=1

# same thing using enumerate
for index, mark in enumerate(marks):
    print(mark)
    if(index == 1): 
        print("Great")
  