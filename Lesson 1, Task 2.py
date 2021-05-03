time = int(input())
sec = time % 60
min = (time // 60) % 60
hr = ((time // 3600) % 3600) % 24 #как введенное число могло бы отобразиться на 24-часовом циферблате
day = (time // 86400) % 365
print('Day(s):', day)
print(hr, 'h :', end=' ')
print(min, 'min :', end=' ')
print(sec, 'sec', end=' ')
