# union()
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.union(s2))
# {1, 2, 3, 4, 5, 6}

# update()
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s1.update(s2)
print(s1)
# {1, 2, 3, 4, 5, 6}

# intersection()
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.intersection(s2))
# {3, 4}

# symmetric_difference()
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1.symmetric_difference(s2)
print(s3)
# {1, 2, 5, 6}

# difference() 
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1.difference(s2)
print(s3)
# {1, 2}

# isdisjoint()
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.isdisjoint(s2))
# False

s1 = {1,2,3,4}
s2 = {5,6}
print(s1.isdisjoint(s2))
# True

# issuperset()
s1 = {1,2,3,4}
s2 = {1,4}
print(s1.issuperset(s2))
# True

# issubset()
s1 = {1,2,3,4}
s2 = {1,4}
print(s2.issubset(s1))
# True

# add()
s1 = {1,2,3,4}
s1.add(5)
print(s1)
# {1, 2, 3, 4, 5}

# remove() / discard()
s1 = {1,2,3,4}
s1.discard(2)
print(s1)
# {1, 3, 4}

# pop()
s1 = {1,2,3,4}
print(s1.pop())
# 1

# del()
s1 = {1,2,3,4}
del s1

# clear()
s1 = {1,2,3,4}
s1.clear()
print(len(s1))
# 0


s1 = {1,2,3,4}
if 4 in s1:
    print("4 is there")
else:
    print("not found")
# 4 is there