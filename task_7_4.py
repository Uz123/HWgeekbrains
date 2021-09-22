import os
from collections import defaultdict


root_dir = 'some_data'
data_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        data_files[size] += 1

for ext, nums in sorted(data_files.items()):
    print(f'{ext}: {nums}')
