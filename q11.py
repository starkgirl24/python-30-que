
total = 0
while True: 
    num = int(input("enter nums:").strip())
    if num == 0:
        break # sentinal: when fun() return this value, iteration stops
    total += num 
print(total)    
    
       