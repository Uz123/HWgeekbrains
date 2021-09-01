duration = int(input('Введите продолжительность времени в секундах '))
day = duration // (24 * 3600)
hours = duration % (24 * 3600) // 3600
minute = duration // 60 % 60
seconds = duration % 60
print(day, 'день', hours, 'часов', minute, 'минут', seconds, 'секунд')
