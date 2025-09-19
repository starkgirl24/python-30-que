line = input("enter a string: ").strip().replace(" ", "").lower()
if line == line[::-1]: #[start : stop : stepsize -1]
    print("is a pallindrom")
else:
    print("NO")    