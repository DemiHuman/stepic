a = str(input('Первое число '))
b = str(input('Второе число '))
c = str(input('Третье число '))

print(max(a,b,c))
print(min(a,b,c))

if min(b,c)<=a<=max(b,c):
    print(a)
elif  min(a,c)<=b<=max(a,c):
    print(b)
elif min(a,b)<=c<=max(a,b):
    print(c)

