from PIL import Image, ImageDraw
import os


def place_box(img_path,img_new_path,box,caption):
    """
    paint boxes on image and resave n
    :param img_path: source image
    :param img_new_path: name for new image with path
    :param box: rectangle that will be drawn
    :param caption: text under rectangle
    :return: nothing, create new image
    """
    if os.path.exists(img_new_path):
        image = Image.open(img_new_path)
    else:
        image = Image.open(img_path)
    tmp = image.copy()
    draw = ImageDraw.Draw(tmp)
    draw.rectangle([box['x0'],box['y0'],box['x1'],box['y1']],outline=(255,0,0,0))
    draw.text([box['x0'],box['y0']-10], caption, (0,0,0,0))
    del draw
    tmp.save(img_new_path)

