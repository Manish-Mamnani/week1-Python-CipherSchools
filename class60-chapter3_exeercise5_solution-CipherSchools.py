n = input("enter your name: ")
b = ""
i = 0
while i < len(n):
    a = n.count(n[i])
    if n[i] not in b:
        b += n[i]
        print(n[i], ":", a)
    i += 1

