import os
import numpy as np

data_dir = '/vision/u/parisz/DepthRegularizedGS/home2'

images_file = os.path.join(data_dir, 'sparse_txt', 'images.txt')

with open(images_file, 'r') as f:
    lines = f.readlines()

contents = lines[4:]

included_names = []
for i, content in enumerate(contents[::2]):
        content_items = content.rstrip('\n').split(' ')
        img_name = content_items[9]
        included_names.append(img_name)

all_names = os.listdir(os.path.join(data_dir, 'images'))
all_names = sorted(all_names)
removed_count = 0
print(included_names)

for name in all_names:
    if name not in included_names:
        os.remove(os.path.join(data_dir, 'images', name))
        print(f"Removed {name}")
        removed_count += 1
    else:
        img_num = int((name.strip().split("."))[0]) - removed_count
        new_name = f"{img_num:05d}.jpg"
        os.rename(os.path.join(data_dir, 'images', name), os.path.join(data_dir, 'images', new_name))
