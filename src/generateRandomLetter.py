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
    return ''.join(word)


def generate_letter_image(word):
    font = ImageFont.truetype(os.path.join(font_path, 'GoodDog.otf'), 120)
    img = Image.open(os.path.join(assets_path, 'number_1.png'))
    draw = ImageDraw.Draw(img)
    print img.size
#     for each in word:
    draw.text((300,300), word, (0,0,0), font=font)
    img.show()


if __name__=='__main__':
    generate_letter_image(generate_random_letter())