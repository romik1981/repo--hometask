#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности durationв секундах:
#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры:
#> duration = 53
#53 сек
#> duration = 153
#2 мин 33 сек
#> duration = 4153
#1 час 9 мин 13 сек
#> duration = 400153
#4 дн 15 час 9 мин 13 сек

# Функция для вычисления интервалов времени
def convert_time(duration):
    if duration < 60:
        return f'{duration} сек' # Выводим количество секунд
    elif duration >= 60 and duration < 3600:
        minutes = duration // 60  # Рассчитаем количество минут
        seconds = duration % 60  # Рассчитаем количество секунд
        return f'{minutes} мин {seconds} сек'
    elif duration >= 3600 and duration < 86400:
        hours = duration // 3600  # Рассчитаем количество часов
        minutes = (duration % 3600) // 60
        seconds = (duration % 3600) % 60
        return  f'{hours} час {minutes} мин {seconds} сек'
    elif duration >= 86400:
        days = duration // 86400  # Рассчитаем количество дней
        hours = (duration % 86400) // 3600
        minutes = (duration % 3600) // 60
        seconds = (duration % 3600) % 60
        return  f'{days} дн {hours} час {minutes} мин {seconds} сек'


duration = int(input('Введите временной интервал в сек: '))
result = convert_time(duration)
print(result)
print(type(result))