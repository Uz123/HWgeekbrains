list_workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']
for idx in range(len(list_workers)):
    name = list_workers[idx].split()
    list_workers[idx] = name
for idx in range(len(list_workers)):
    print(f'Привет, {list_workers[idx][-1].title()}!')
