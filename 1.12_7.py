a = input().split

for i in range(len(a)):
    a[i] = int(a[i])

if a[1]+a[2]+a[3] == a[4]+a[5]+a[6]:
    print('Счастливый')
else:
    print('Обычный')
