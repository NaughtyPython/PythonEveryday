'''
iphone5: 1136 x 640

use the following code to get the filename:
    filename in next(os.walk(os.path.join(BASE_PATH, "..","assets","Images")))[2]
'''

from PIL import Image

import os


BASE_PATH = os.path.dirname(__file__)

for filename in next(os.walk(os.path.join(BASE_PATH, "..","assets","Images")))[2]:
    print filename
    image_path = os.path.abspath(os.path.join(BASE_PATH, '..','assets','Images', filename))
    print image_path
    img = Image.open(image_path)
    width, length = img.size
    if width>640 or length>1136:
        resize = 640, 1136
        img.thumbnail(resize)
    print img.size
    img.show()
