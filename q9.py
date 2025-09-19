start = int(input("enter num start: ").strip())
end = int(input("enter end:").strip())
step = int(input("enter step size:"))
total = 0
for i in range(start, end, step): 
    total += i*i  # total = total +(i*i)
print("total sum :", total)  

# start = int(input("enter num start: ").strip())
# end = int(input("enter end:").strip())
# step = int(input("enter step size:"))
# total = 0
# for i in range(start, end+1, step): 
#     total += i*i  # total = total +(i*i)
# print("total sum :", total)   