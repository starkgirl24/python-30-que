n  = int(input("enter num: "))
steps = 0
while (n != 1):
    print(n,end="->") #for sequence
    if(n % 2 == 0):
        n = n//2
    else:
        n = 3* n + 1
    steps += 1
print(1)    #last value 1  
print("total steps:",steps)            


# def collatz(num):
#     if num ==1:
#         return[num]
    
#     seq = []
#     if(num % 2 == 0):
#         seq = collatz(num//2)
#     else:
#         seq = collatz(3*num+1)
#     steps =  [num] + seq
#     return steps   
# if __name__ == "__main__":
#     print(collatz(6))            