list_hw = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx, item in enumerate(list_hw):
    if item.isdigit() or item[0] == '+' or item[0] == '-' and item[1:].isdigit():
        list_hw[idx] = '"'+item+'"'
mes = " ".join(list_hw)
print(mes)
