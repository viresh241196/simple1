import sys
import os
from PIL import Image

# From = sys.argv[1]
# to = sys.argv[2]
#
#
# if os.path.exists(to):
#     pass
# else:
#     os.mkdir(to)            # C:\\Users\hp\Desktop\images
#
# all_items = os.listdir(From)
#
# for item in all_items:
#     image = Image.open(f'{From}{item}')
#     clean_name = os.path.splitext(item)[0]
#     image.save(f'{to}{clean_name}.png','png')
#     print('done')
#


image = Image.open('G:\\study\photo.png')
print(image)
if image.height > 300 or image.width > 300:
    output_size = (35,35)
    image.thumbnail(output_size)
    image.save('H:\\photo','JPG')
    print('done')
else:
    print('error')