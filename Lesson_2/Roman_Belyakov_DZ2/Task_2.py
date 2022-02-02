"""
Задание 2
На вход будет выдаваться список, пример:

['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка,
являющегося числом) и дополнить нулём до двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
b) Сформировать из обработанного списка строку:

в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

"""

def convert_list_in_str(list_in: list) -> str:
    new_list = []
    for some_str in list_in:
        if some_str.isdigit():
            some_str = int(some_str)
            new_list.append(f'"{some_str:02d}"')
        elif some_str[0] == '+':
            some_str = int(some_str[1:])
            new_list.append(f'"+{some_str:02d}"')
        elif some_str[0] == '-':
            some_str = int(some_str[1:])
            new_list.append(f'"-{some_str:02d}"')
        else:
            new_list.append(some_str)
    str_out = ' '.join(new_list)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)