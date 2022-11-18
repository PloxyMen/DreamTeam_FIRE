import random as rd
random_number = rd.randint(0,10)
p = 0
while p<3:
  a = int(input('угадайте число от 0 до 10: '))
  if a == random_number:
    print('Вы угадали число')
    print(f'Случайное число-{random_number}')
    break
  if a != random_number:
    p+=1
    if p==3:
      print(f'Вы не угадали число, загаданное число-{random_number}')
