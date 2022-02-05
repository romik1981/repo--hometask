""""
Задание 5
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

"""
# первый вариант
#result = []
#for num in src:
#    if src.count(num) == 1:
#        result.append(num)
#return result

# Второй вариант
# result = [num for num in src if src.count(num) == 1]
#    return result

# Третий вариант
def get_uniq_numbers(src: list):
    unique_numbers = set()
    tmp = set()
    for num in src:
        if num not in tmp:
           unique_numbers.add(num)
        else:
           unique_numbers.discard(num)
        tmp.add(num)
    result = [num for num in src if num in unique_numbers]
    return result


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))