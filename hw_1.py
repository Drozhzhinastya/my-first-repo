input_number = input('Вам будет продемонстрирован фокус. Какое бы число вы не ввели, ряд арифметических операций превратит его в 4. Итак, начнем! Введите свое число: ')
number = int(input_number)
print('1) Число', number, 'умножим на 2, получим', number * 2)
print('2) К числу', number * 2, 'добавим 8, получим', number * 2 + 8)
print('3) Теперь разделим полученный результат на 2, получаем', (number * 2 + 8) // 2)
print('4) Число', (number * 2 + 8) // 2, 'минус', number, 'равно', (number * 2 + 8) // 2 - number)
print('Мы получили 4!')
