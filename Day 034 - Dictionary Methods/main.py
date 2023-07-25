team1 = {
    10 : 56, 
    11 : 42,
    12 : 90,
    13 : 99
}

team2 = {
    14 : 66,
    15 : 87
}

team1.update(team2)
print(team1)

# Output : {10: 56, 11: 42, 12: 90, 13: 99, 14: 66, 15: 87}

team2.clear()
print(team2) 
# Output : {}

# We can also create a empty dictionary
emp = {}

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
# {'name': 'Karan', 'age': 19, 'eligible': True}
info.update({'DOB':2001})
print(info)
# {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
# {'name': 'Karan', 'age': 19}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
# {'name': 'Karan', 'age': 19, 'eligible': True}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
# {'name': 'Karan', 'eligible': True, 'DOB': 2003}

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info)
# NameError: name 'info' is not defined