n = int(input("enter num:").strip())
out = []
for i in range(1,n+1):
    if(i %3 == 0):
        continue
    out.append(str(i)) #string coz output space
print(" ".join(out))    

