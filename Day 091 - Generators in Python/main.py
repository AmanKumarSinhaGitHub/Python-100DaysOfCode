def my_generator():
    for i in range(5):
        yield i


gen = my_generator()
# print(next(gen)) # 0
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3
# print(next(gen)) # 4


for j in gen:
    print(j)

# Same output : 0 1 2 3 4 