def real_work_stations():
    """
    Алгоритм просчёта выработки товара с 2х машин, с расчета начала/конца их работы и заданного цикла на каждой из них
    :return:
    """
    # Запрашиваем время начала работы машин
    start_time_hours = int(input('Введите текущее время: Часы:  '))  # Starting Time Hours
    start_time_minutes = int(input('Введите текущее время: Минуты:  '))  # Starting Time Minutes
    start_time_seconds = int(input('Введите текущее время: Секунды:  '))  # Starting Time Seconds
    # Запрашиваем время окончания работы машин
    end_time_hours = int(input('Введите время окончания работы: Часы:  '))  # Ending Time Hours
    end_time_minutes = int(input('Введите время окончания работы: Минуты:  '))  # Ending Time Minutes
    end_time_seconds = int(input('Введите время окончания работы: Секунды:  '))  # Ending Time Seconds
    # Запрашиваем циклы работы машин, для дальнейших подсчётов (за 1 цикл 1 машина изготавливает 8 шт. товара)
    cycle_1 = float(input('Введите цикл первой машины:  '))
    cycle_2 = float(input('Введите цикл второй машины:  '))
    # Просчитываем общее время работы в секундах
    end_day_seconds = end_time_hours * 3600 + end_time_minutes * 60 + end_time_seconds  # End Day Time in sec.
    start_day_seconds = 86400 - (start_time_hours * 3600 + start_time_minutes * 60 + start_time_seconds)  # One Day sec.
    total_time_seconds = end_day_seconds + start_day_seconds  # TotalSum StartTime + EndTime
    # Приводим общее время в секундах в привычный формат
    work_seconds = total_time_seconds
    work_hours = work_seconds // 3600
    work_seconds = work_seconds - (work_hours * 3600)
    work_minutes = work_seconds // 60
    work_seconds = work_seconds - (work_minutes * 60)
    # Просчитываем в цикле по получившимся общ. секундам каждую машину по отдельности (т.к. цикл у каждой свой)
    per_seconds_1 = 0  # it's work 1 Station (Переменная будет накапливать секунды)
    total_cycle_1 = 0  # it's work 1 Station (Переменная будет накапливать циклы)
    # 'Прогоняем' полностью работу 1ой машины за все отведенное время(по сути виртуальная работа за смену, за доли сек.)
    for x in range(total_time_seconds):  # it's work 1 Station
        per_seconds_1 += 1  # С каждой итерацией прибавляет переменной секунду
        if per_seconds_1 >= cycle_1:
            per_seconds_1 -= cycle_1
            total_cycle_1 += 1  # С накоплением секунд, равных или больше циккла, добавляет цикл

    per_seconds_2 = 0  # it's work 2 Station
    total_cycle_2 = 0  # it's work 2 Station
    # 'Прогоняем' полностью работу 2ой машины за все отведенное время(по сути виртуальная работа за смену, за доли сек.)
    for x in range(total_time_seconds):  # it's work 2 Station
        per_seconds_2 += 1
        if per_seconds_2 >= cycle_2:
            per_seconds_2 -= cycle_2
            total_cycle_2 += 1
    # Делаем итоговые вычисления
    total_bottle_1 = total_cycle_1 * 8  # Общее кол-во товара в штуках с 1ой машины
    total_bottle_2 = total_cycle_2 * 8  # Общее кол-во товара в штуках со 2ой машины
    total_bottle = total_bottle_1 + total_bottle_2  # Общее итоговое кол-во в штуках

    total_package_1 = total_bottle_1 / 248  # Общее кол-во товара в упаковках с 1ой машины
    total_package_1_test = total_cycle_1 // 31  # Testing Score
    total_package_2 = total_bottle_2 / 248  # Общее кол-во товара в упаковках со 2ой машины
    total_package_2_test = total_cycle_2 // 31  # Testing Score
    total_package = total_package_1 + total_package_2  # Общее итоговое кол-во в упаковках
    test_total_all_package = total_package_1_test + total_package_2_test

    total_material_station1 = total_package_1 * 8.03  # Выработанное сырьё с 1ой машины
    total_material_station2 = total_package_2 * 8.03  # Выработанное сырьё со 2ой машины
    total_material = total_material_station1 + total_material_station2  # Общее количество выработанного сырья
    # Выводим все нужные результаты на экран
    print(f'\nИтого с 1 машины: {total_bottle_1} шт. товара, {"%.2f" %total_package_1} уп. товара '
          f'(тест{total_package_1_test})'
          f'\nИзрасходовано {"%.2f" %total_material_station1} кг. сырья (testTime {"%.2f" %per_seconds_1})')
    print(f'Итого со 2 машины: {total_bottle_2} шт. товара, {"%.2f" %total_package_2} уп. товара '
          f'(тест{total_package_2_test})'
          f'\nИзрасходовано {"%.2f" %total_material_station2} кг. сырья (testTime {"%.2f" %per_seconds_2})')
    print(f'\nВсего: {total_bottle} шт. ({test_total_all_package*248}) товара, {"%.2f" %total_package} уп. товара '
          f'\nИзрасходовано {"%.2f" %total_material} кг. ({"%.2f" %(total_material / 25)} уп.) сырья')
    print(f'\nВремя начала работы: {start_time_hours} часов {start_time_minutes} минут {start_time_seconds} секунд')
    print(f'Время окончания работы: {end_time_hours} часов {end_time_minutes} минут {end_time_seconds} секунд')
    print(f'Общее время работы: {work_hours} часов {work_minutes} минут {work_seconds} секунд')
    print(f'totalsec{total_time_seconds}')


real_work_stations()
