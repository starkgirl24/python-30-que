n = int(input("enter num"))
lst = list(map(int, input().split()))
k = int(input())
if n > 0:
    k = k%n
else:
    k = 0 # no rotation
if k == 0:
    rotated = lst
else:
    rotated = lst[-k:] + lst[:-k]  
    print(rotated)          