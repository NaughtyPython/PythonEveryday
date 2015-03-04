import string
import random
import os
from path import assets_path, font_path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def generate_random_letter():
    word = []
    for _i in range(4):
        word.append(random.choice(string.letters))
    return word


def generate_letter_image(word):
    font = ImageFont.truetype(os.path.join(font_path, 'GoodDog.otf'), 120)
    img = Image.open(os.path.join(assets_path, 'number_1.png'))
    draw = ImageDraw.Draw(img)
    print img.size
    x = 200
    y = 200
    color_x = 0
    color_y = 0
    color_z = 0
    for each in word:
        x = x + 50
        color_x = color_x + 50
        color_y = color_y + 20
        color_z = color_z + 30
        draw.text((x,y), each, (color_x,color_y,color_z), font=font)
    img.show()


if __name__=='__main__':
    generate_letter_image(generate_random_letter())