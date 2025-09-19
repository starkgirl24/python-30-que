line = input().strip()
words = [ w.lower() for w in line.split()]

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
        
result = {k : freq[k] for k in sorted(freq)}
print(result)            