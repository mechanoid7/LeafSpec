import os

from PIL import Image


def handle(image_path, width=1200, height=1200):  # in work

    # set_path = image_path.replace(r"/", "\\")  # изменить путь
    # image_path = image_path.replace(r"/", "\\")  # изменить путь
    # image_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+set_path
    # image_path = 'F:\\Download\\Снимок.png'
    original_image = Image.open(image_path)
    w, h = original_image.size
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    image_path = image_path.rsplit(".", 1)
    image_path = image_path[0]+"_resize."+image_path[1]
    original_image.save(image_path)
    return image_path

