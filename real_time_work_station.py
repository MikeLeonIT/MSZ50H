def real_time_work_station():
    nowhours = int(input('Введите текущее время: часов  '))
    nowminuts = int(input('Введите текущее время: минут  '))
    nowseconds = int(input('Введите текущее время: секунд  '))

    cickle = float(input('Введите заданный цикл: '))

    totalproduckt = int(input('Введите желаемое количество готовых упаковок: '))
    totalbuttle = totalproduckt * 248

    totalcickle = totalbuttle // 8
    totalcickle2 = totalproduckt * 31

    totaltimesec = totalcickle * cickle

    totalmaterial = totalproduckt * 8.03

    seconds = totaltimesec
    hours = seconds // 3600
    seconds = seconds - (hours * 3600)
    minuts = seconds // 60
    seconds = seconds - (minuts * 60)

    startendsec = totaltimesec + (nowhours * 3600) + (nowminuts * 60) + nowseconds

    endsec = 0
    endmin = 0
    endhour = 0
    endday = 0
    for x in range(int(startendsec)):
        endsec += 1
        if endsec == 60:
            endsec = 0
            endmin += 1
        if endmin == 60:
            endmin = 0
            endhour += 1
        if endhour == 24:
            endhour = 0
            endday += 1
    print(f'Текущее время: {nowhours} часов {nowminuts} минут {nowseconds} секунд')
    print(f'Ожидаемое количество готовых упаковок: {totalproduckt} упаковок ({totalbuttle} бутылок)')
    print(f'Ожидаемое количество использованного сырья: {totalmaterial} килограмм')
    print(f'Ожидаемое количество циклов: {totalcickle} (TEST {totalcickle2})')
    print(f'Ожидаемое количество секунд: {totaltimesec}')
    print(f'Ожидаемое затраченное время: {int(hours)} часов {int(minuts)} минут {seconds} секунд')
    print(f'Время окончания работы: {endhour} часов {endmin} минут {endsec} секунд (+{endday} дней)')


real_time_work_station()
