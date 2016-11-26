a = input()

if len(a) == 6:
    b = int(a[0])+int(a[1])+int(a[2])
    d = int(a[3])+int(a[4])+int(a[5])
    if b == d:
        print('Счастливый')
    else:
        print('Обычный')
else:
    print('Только строка в 6 символов')