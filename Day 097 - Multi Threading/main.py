import threading
import time

#indicate some task being done
def sleepFunc(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# without multithreading
# sleepFunc(4)
# sleepFunc(5)
# sleepFunc(2) 

# with multithreading
t1 = threading.Thread(target=sleepFunc, args=[4])
t2 = threading.Thread(target=sleepFunc, args=[5])
t3 = threading.Thread(target=sleepFunc, args=[2])

t1.start()
t2.start()
t3.start()

print("task started")

t1.join()
t2.join()
t3.join()

print("Task end")