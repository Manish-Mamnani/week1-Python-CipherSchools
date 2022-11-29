n = input("enter a number containing more than 1 digit: ")
sum = 0
i = 0
while i < len(n):
    sum += int(n[i])
    i += 1
print(sum)