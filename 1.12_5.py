a = int(input())
b = int(input())
c = int(input())

if a > b > c:
    print(a)
    print(c)
    print(b)

elif a > c > b:
    print(a)
    print(b)
    print(c)

elif b > c > a:
    print(c)
    print(b)
    print(a)

elif c > b > a:
    print(c)
    print(a)
    print(b)
