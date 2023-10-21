import time

t = time.localtime()
formatted_time = time.strftime("Date: %d-%m-%Y   Time: %H:%M:%S", t)

print(formatted_time)
# Output: Date: 21-10-2023   Time: 11:02:32



time.sleep(5)
print("this is printed after 5 second")