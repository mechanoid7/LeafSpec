import os
import pathlib
from NeuralNetwork.apps.neuralmain.bin.scripts import label_image
from .plants_list import translate_dict


def translate(name):
    """ Function get dict from 'plants_list.py' -> translate_dict. Search coincidences and translate ENG to RUS,
    else - leaves current name """

    try:
        translated_name = translate_dict[name]  # try get RUS name from dict[key]
    except Exception:
        translated_name = name  # leaves current name
    return translated_name


def compose_answer(analyze_data):
    """ This function analyse answer from TensorFlow and draws conclusions """

    # in RELEASE delete - > {analyze_data[1][1]:.2f}
    return_data = f''
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
        return_data += 'Мы не можем понять, что это('
    return_data += f' Время выполнения: {analyze_data[0]}. '

    return return_data


def detect_image(img_name):
    img_path = str(pathlib.Path(__file__).parent.absolute()).replace('\\NeuralNetwork\\apps\\neuralmain\\tools', '')\
               + str(img_name).replace('/', '\\')  # set path to IMAGE in requests
    analyze_data = label_image.run_analyse(img_path)  # analyzing photo
    return_data = compose_answer(analyze_data)  # compose answer

    return return_data













# python {PATH}scripts/label_image.py --image {PATH}img.jpg
