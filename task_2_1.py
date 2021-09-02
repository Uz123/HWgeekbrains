raw = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
for idx, val in enumerate(raw, start=1):
    print(f'№ {idx} => {val:<5} имеет {type(val)}')
