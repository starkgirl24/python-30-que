n = int(input().strip())
for _ in range(n):
    line = input()
    if "#" in line:
        line = line.split('#',1)[0]
    line = line.rstrip()  #from end removesspaces,trailing \n  will be removed 
    if line:  #will skil empty lines
        print(line)    
    

