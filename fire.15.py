x = float(input('напишите вклад->'))
z = int(input('напишите срок->'))
y = 10
for i in range (z):
    s = x / 100 * y
    x += s
print(f'на вашем счету - {x} рублей')
