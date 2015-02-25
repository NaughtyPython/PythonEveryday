'''
if img.show() not works, please install the following:
    sudo apt-get install imagemagick


1. open the two images in assets/
2. create thumbnail of image and save to dir
3. paste the image to the background image
4. show the image
'''

from PIL import Image
import os


def generateUnreadMessageImage():
    base_path = os.path.dirname(__file__)
    print base_path
    file_path = os.path.abspath(os.path.join(base_path, "..", "assets", "Tencent_QQ.png"))
    print file_path
    file_path2 = os.path.abspath(os.path.join(base_path, "..", "assets", "number_1.png"))

    background = Image.open(file_path)
    back_w, back_h = background.size
    print background.size

    # set the size of thumbnail
    size = (back_w + back_h)/(2*10), (back_w + back_h)/(2*10)
    img = Image.open(file_path2)
    img.thumbnail(size)
    # img.save(file_path2)
    img_w, img_h = img.size
    print img_w, img_h

    # set the position of the image
    offset = ((back_w - img_w)*7/8, (back_h - img_h)/8)
    background.paste(img, offset)
    background.show()


if __name__ == '__main__':
    generateUnreadMessageImage()