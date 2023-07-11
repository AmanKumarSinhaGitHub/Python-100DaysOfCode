# Changing tuple indirectly using LIST
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item at last
temp.pop(3)                 # remove the item at index 3, which is "England"
temp[2] = "Finland"         # change item "India" to "Finland" at index 2
countries = tuple(temp)
print(countries)            # ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')


# concatenate two tuples without converting them to list.
countries = ("India", "Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# All operations are same as list