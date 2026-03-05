#!/usr/bin/env python3
from PIL import Image
import sys
img = Image.open(sys.argv[1])
img.save(sys.argv[1].replace('.jpg','_c.jpg'),'JPEG',quality=70)
print("完成")
