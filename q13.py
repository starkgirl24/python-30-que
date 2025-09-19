n = int(input("enter").strip())
count = 0
vowels  = set('aeiou')
for _ in range(n):
    word = input("enter word")
    if word and word[0].lower() in vowels:
        count += 1
    else:
        pass
print(count)        