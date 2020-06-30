"""Image file analyse in this module

    :Date: 24-04-2020
    :Version: Beta
    :Authors:
        - Mechanoid
"""

import pathlib

from NeuralNetwork.apps.neuralmain.bin.scripts import label_image
from .plants_list import translate_dict
from .file_manipulator import move_to_dir


def translate(name):
    """ Function get dict from 'plants_list.py' -> translate_dict. Search coincidences and translate ENG to RUS, else - leaves current name
    - Parameters:
        :name(str): type of plant which should be translated

    - Returns:
        :translated_name(str): if name exist - translated name, else - current name
    """
    try:
        translated_name = translate_dict[name]  # try get RUS name from dict[key]
    except Exception:
        translated_name = name  # leaves current name
    return translated_name


def compose_answer(analyze_data, img_path, **kwargs):
    """ Function analyse answer from TensorFlow and draws conclusions
    - Parameters:
        :analyze_data(list): input two-dimensional array which has the appearance of a plant and a match rate

        :img_path(str): path to img file

    - Returns:
        :return_data(str): msg(possible plant type, chance) and file processing time
    """
    # in RELEASE delete - > {analyze_data[1][1]:.2f}
    return_data = f''  # it`s a 'Answer' variable
    continue_compose = False
    try:  # if kwargs haven`t USER_TYPE - skip this step
        if kwargs['user_type']:
            if analyze_data[1][1] > 0.5:
                # if img determined with high accuracy name the folder with the name of a specific plant / user_type
                temp_path = analyze_data[1][0]+'\\'+kwargs['user_type']
            else:
                # else name the folder is 'unknown' / user_type
                temp_path = 'unknown\\'+kwargs['user_type']
            move_to_dir('img_to_database\\'+temp_path, img_path)
    except:
        continue_compose = True

    if continue_compose:
        print("Checkpoint compose start - OK")
        if analyze_data[1][1] > 0.9:
            return_data += f'Это "{translate(analyze_data[1][0])}" - {analyze_data[1][1]:.2f}.'
        elif analyze_data[1][1] > 0.6:
            return_data += f'Вероятнее всего это "{translate(analyze_data[1][0])}" - {analyze_data[1][1]:.2f}.'
        elif analyze_data[1][1] > 0.4:
            return_data += f'Возможно это "{translate(analyze_data[1][0])}" - {analyze_data[1][1]:.2f}.'
        elif analyze_data[1][1] > 0.25:
            return_data += f'Это немного похоже на "{translate(analyze_data[1][0])}" - {analyze_data[1][1]:.2f}'
            if analyze_data[2][1] > 0.25:
                return_data += f' и на "{translate(analyze_data[2][0])}" - {analyze_data[2][1]:.2f}.'
        else:
            return_data += 'Мы не можем понять, что это :(   '
        print("Checkpoint compose end - OK")

        if analyze_data[1][1] > 0.6:
            move_to_dir(second_path='requests\\'+analyze_data[1][0], img_path=img_path)  # if chance > 0.6(60%) move file to <img_type> folder
        else:
            move_to_dir(second_path='requests\\trash', img_path=img_path)  # if chance < 0.6(60%) move file to trash box
        print("Checkpoint compose move - OK")

        return_data += f' Время выполнения: {analyze_data[0]}. '

    return return_data


def detect_image(img_name, **kwargs):
    """ Function processes and defines the plant in the photograph.
    - Parameters:
        :img_name(str): name of img file

    - Returns:
        :return_data(str): answer(message have type of plant and processing time)
    """
    img_path = str(pathlib.Path(__file__).parent.absolute()).replace('\\NeuralNetwork\\apps\\neuralmain\\tools', '')\
               + str(img_name).replace('/', '\\')  # set path to IMAGE in requests
    # print('>>>IMG_PATH:', img_path)
    analyze_data = label_image.run_analyse(img_path)  # analyzing photo
    print("Checkpoint DETECT - OK")

    return_data = compose_answer(analyze_data, img_path, **kwargs)  # compose answer
    print("Compose answer - OK")

    return return_data


def save_user_upload(img_name, **kwargs):
    """
    :param img_name:
    :param kwargs:
        user_type: type of plant which user set
    :return:
    """
    try:
        detect_image(img_name, **kwargs)
    except:
        pass










# python {PATH}scripts/label_image.py --image {PATH}img.jpg
