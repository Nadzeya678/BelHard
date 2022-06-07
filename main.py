# 3 numbers
a = input('Input value a:')
b = input('Input value b:')
c = input('Input value c:')
a = float(a)
b = float(b)
c = float(c)
if a<b and a<b:
    mini = a
elif b<c and b<a:
    mini = b
elif c<b and c<a:
    mini = c
if b>a and b>c:
    maxi = b
elif a>b and a>c:
    maxi = a
elif c>a and c>b:
    maxi = c
if b>a and b<c:
    midi = b
if c>a and c<b:
    midi = c
if a>b and a<c:
    midi = a
if mini < 1 and mini % 2 != 0:
    print('Самое маленькое число меньше единицы и нечетное, введите цифры заново')
    print(maxi)
if maxi < (mini+midi)/2 or maxi > (mini*midi):
    print('Самое большое число не соответсвует условию, введите цифры заново')
if midi % 3 != 0 and midi % 2 != 0:
    print('Среднее число не соответствует условию')
else:
    print(f'Наибольшее -  {maxi}, среднее - {midi}, наименьшее - {mini}')
