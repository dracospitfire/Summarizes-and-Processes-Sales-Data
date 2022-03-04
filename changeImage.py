#!/usr/bin/env python3

import os
from PIL import Image

path = "supplier-data/images"

for image in os.listdir(path):
    if image.endswith('tiff'):
        print(image)
        i = Image.open(os.path.join(path, image))
        file, ext = os.path.splitext(image)
        i = i.convert("RGB")
        i = i.resize((600, 400))
        i.save('supplier-data/images/{}.jpeg'.format(file))
