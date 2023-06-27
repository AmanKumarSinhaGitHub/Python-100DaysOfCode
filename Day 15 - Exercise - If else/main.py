# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

from datetime import datetime

current_hour = datetime.now().hour

if(current_hour>=4 and current_hour<12):
    print("Good Morning")
elif(current_hour>=12 and current_hour<=17):
    print("Good Afternoon")
elif(current_hour>=17 and current_hour<=21):
    print("Good Evening")
else:
    print("Good Night")


