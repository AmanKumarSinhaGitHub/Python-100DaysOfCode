from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n

print(fx(20))
print("Executed in 5 Sec")
print(fx(10))
print("Executed in 5 Sec")
print(fx(15))
print("Executed in 5 Sec")


print("\nExcuted in less than 1 sec because these values are already cached")
print(fx(10))
print(fx(15))
print(fx(20))