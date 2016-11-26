a = int(input())
b = int(input())
c = int(input())

d = max(a,b,c)
f = min(a,b,c)

print(d)
print(f)

if min(b,c)<=a<=max(b,c):
    print(a)
elif min(a,c)<=b<=max(a,c):
    print(b)
elif min(a,b)<=c<=max(a,b):
    print(c)
