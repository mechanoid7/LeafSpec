import os
import pathlib
import shutil
from NeuralNetwork.apps.neuralmain.bin.scripts import label_image
from .plants_list import translate_dict


def move_to_dir(plant_type, img_path):
    """ This function move image to directory which has a name <plant_type> or create new der and move"""
    requests_path = str(pathlib.Path(__file__).parent.absolute()).replace('NeuralNetwork\\apps\\neuralmain\\tools', '') \
                    + 'media\\requests\\'  # path to requests
    plant_dir_path = requests_path + str(plant_type)  # path to pequests\<plant_type>
    if os.path.isdir(plant_dir_path):  # if the folder exists
        shutil.move(img_path, plant_dir_path)  # image move
    else:
        os.mkdir(plant_dir_path)  # folder create
        shutil.move(img_path, plant_dir_path)  # image move


def translate(name):
    """ Function get dict from 'plants_list.py' -> translate_dict. Search coincidences and translate ENG to RUS,
    else - leaves current name """

    try:
        translated_name = translate_dict[name]  # try get RUS name from dict[key]
    except Exception:
        translated_name = name  # leaves current name
    return translated_name


def compose_answer(analyze_data, img_path):
    """ This function analyse answer from TensorFlow and draws conclusions """

    # in RELEASE delete - > {analyze_data[1][1]:.2f}
    return_data = f''  # it`s a 'Answer' variable
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

    if analyze_data[1][1] > 0.6:
        move_to_dir(analyze_data[1][0], img_path)  # if chance > 0.6(60%) move file to <img_type> folder
    else:
        move_to_dir('trash', img_path)  # if chance < 0.6(60%) move file to trash box


    return_data += f' Время выполнения: {analyze_data[0]}. '

    return return_data


def detect_image(img_name):
    img_path = str(pathlib.Path(__file__).parent.absolute()).replace('\\NeuralNetwork\\apps\\neuralmain\\tools', '')\
               + str(img_name).replace('/', '\\')  # set path to IMAGE in requests
    # print('>>>IMG_PATH:', img_path)
    analyze_data = label_image.run_analyse(img_path)  # analyzing photo
    return_data = compose_answer(analyze_data, img_path)  # compose answer

    return return_data













# python {PATH}scripts/label_image.py --image {PATH}img.jpg
