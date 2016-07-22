f = str(input('Фигура '))

if f == 'треугольник':
    a = float(input('Первое число '))
    b = float(input('Второе число '))
    c = float(input('Третье число '))
    p = (a+b+c) / 2
    import math
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)

elif f == 'прямоугольник':
    a = float(input('Первое число '))
    b = float(input('Второе число '))
    S = a * b
    print(S)
elif f == 'круг':
    r = float(input('Радиус '))
    S = 3.14 * (r ** 2)
    print(S)
