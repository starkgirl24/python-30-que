num = int(input("how many nums: "))
out = []
for _ in range(num):
    out.append(int(input("enter your num")))
    cubes = [x **3 for x in out] #in list
print(cubes)    
    
    
