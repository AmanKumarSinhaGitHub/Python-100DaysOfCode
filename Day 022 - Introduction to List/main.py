marks = [30,58,46] 
print(marks)
print(type(marks))

print(marks[0]) # 30

list = [10, "Ten", False, 5.6, "Hello Aman", 46]
print(list)


# Negative Indexing
print(list[-2]) 
# print(list[len(list)-2])
# print(list[6-2])
# print(list[4])
# Output : "Hello Aman"


# Check an item is present or not
if 10 in list:
    print("Yes")

#print list
list = [10,20,30,40,50,60,70,80]
print(list)
print(list[:])

# print list form index 2 - 6
print(list[2:7])

# Jump index
# print list from index 1 to 3 with jumb of 2
print(list[1:4:2]) # [20, 40]

# List Comprehension
list = [i for i in range(4)]
print(list) # [0, 1, 2, 3]

list = [i+5 for i in range(4)]
print(list) # [5, 6, 7, 8]

# make a list of even no.
list = [i for i in range(13) if(i%2==0)]
print(list) # [0, 2, 4, 6, 8, 10, 12]
