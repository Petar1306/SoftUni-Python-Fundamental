start = int(input())
stop = int(input())
for i in range(start, stop+1):
    if i == stop:
        print(chr(i))
    else:
        print(chr(i), end=" ")
