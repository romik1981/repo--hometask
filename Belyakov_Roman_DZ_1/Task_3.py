#Реализовать склонение слова процент во фразе N процентов. Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов
#...
#100 процентов

def transform_string(n):
    if n == 1:
        return f'{n} процент'  # верните отформатированную строку
    elif n >= 5 and n <= 20:
        return f'{n} процентов'
    elif n % 10 == 1:
        return f'{n} процент'
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        return f'{n} процента'
    elif n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or n % 10 == 0:
        return f'{n} процентов'

for n in range(1, 101):
    print(transform_string(n)) # по заданию учитываем только значения от 1 до 100