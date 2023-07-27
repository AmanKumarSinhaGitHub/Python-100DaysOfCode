# This will print value form 2 to 4 and after that because loop ends, it will go to else statement
for i in range(2, 5):
    print(i)
else :
    print("Loop ends")

''' 
Output :
2
3
4
Loop ends '''


# By seeing this example, you can understand that else will only execute when loop successfully completed its all iteration or ends, not when loop break or terminate
for i in range(2, 10):
    print(i)
    if(i==4):
        break
else:
    print("Out of loop")

'''
Output :
2
3
4
'''


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

'''
Output :
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
'''


# You can also use the else with while loop