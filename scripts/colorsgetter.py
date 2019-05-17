from PIL import Image, ImageDraw


def get_colors(file, numcolors=4, swatchsize=50, resize=150):
    """
    get main colors from image and put boxes on it

    :param file: source file
    :param numcolors:
    :param swatchsize: sixe of boxes
    :param resize: not matter
    :return: nothing
    """
    image = Image.open(file)
    image_resized = image.resize((resize, resize))
    result = image_resized.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize * resize)

    # Save colors to file

    pal = Image.new('RGB', (swatchsize * numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx + swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    del draw
    image.paste(pal)

    image.save(file)


def put_colors(img_path, img_new_path, box):
    """
     crops img and put on it boxes with main colors

    :param img_path: source image
    :param img_new_path: path for new image
    :param box: crop box dict(x0,x1,y0,y1)
    :return: nothing - create image
    """
    img = Image.open(img_path)
    new_size = [box['x0'], box['y0'], box['x1'], box['y1']]
    new_img = img.crop(new_size)
    new_img.save(img_new_path)
    get_colors(img_new_path)