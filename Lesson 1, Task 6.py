first_day = int(input())
at_least = int(input())
while first_day <= at_least:
    print((first_day * 0.1) + first_day)
    first_day = (first_day * 0.1) + first_day
