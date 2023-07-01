print("Break statement terminate the code when i = 6")
for i in range(1, 10):
    if i == 6:
        break
    print(i)

print("Continue statement skips printing 3 and print rest of the code")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)