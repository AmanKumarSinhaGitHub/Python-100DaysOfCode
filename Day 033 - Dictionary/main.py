students = [
    {
        "Name": "Aman Kumar Sinha",
        "Roll": 48,
        "College": "R.N College"
    },

    {
        "Name": "Rohan",
        "Roll": 25,
        "College": "ABC University"
    },
    
]

# Accessing elements of the first student in the list
print("Name:", students[0]["Name"])
print("Roll:", students[0]["Roll"])
print("College:", students[0]["College"])

''' Output : 
Name: Aman Kumar Sinha
Roll: 48
College: R.N College'''

roll = {
    45 : "Alok",
    32 : "Rohan"
}

print(roll[45]) # Alok


info = {
    'name' : 'Karan', 
    'age' : 22,
}

for key in info.keys():
    print(info[key])

# Karan
# 22

