num = int(input())
big = num % 10
num = num // 10
while num > 0:
    if num % 10 > big:
        big = num % 10
    num = num // 10
print(big)

