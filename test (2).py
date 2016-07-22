m = int(input('Кол-во минут сна '))
H = int(input('Час - когда легла '))
Min = int(input('Минуты - когда легла '))
ch = m // 60
minut = m % 60
minut += Min
chas = ch + H + (minut // 60)
minut %= 60
print(chas)
print(minut)


#    m = int(input('Кол-во минут сна'))
#    H = int(input('Час - когда легла'))
#    Min = int(input('Минуты - когда легла'))
#    minut = m % 60
#    minut += Min
#    ch = (m // 60) + (minut // 60) + H
#    print(ch)
#    print(minut)
