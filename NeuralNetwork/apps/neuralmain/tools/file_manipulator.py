""" This module makes it possible to check file extension and name, delete file

    :Date: 24-04-2020
    :Version: Beta
    :Authors:
        - Mechanoid
"""

import pathlib
import re, os
import shutil
from random import choice
from string import ascii_letters


def move_to_dir(second_path, img_path):
    """ This function move image to request directory which has a name <second_path> or create new dir and move

    - Parameters:
        :second_path(str): where - path where you want to move the file
        :img_path(str): what - path to img file

    !use only in MEDIA!
    """
    move_to_path = 'media\\'

    media_path = str(pathlib.Path(__file__).parent.absolute()).replace('NeuralNetwork\\apps\\neuralmain\\tools', '') \
                    + move_to_path  # path to requests
    plant_dir_path = media_path + str(second_path)  # path to requests\<second_path>
    try:
        if os.path.isdir(plant_dir_path):  # if the folder exists
            while True:
                try:  # try move file to dir
                    shutil.move(img_path, plant_dir_path)  # move img ti folder
                    break
                except:  # if file is exist
                    print("Img path after:", img_path)
                    img_path = rename_file(img_path)
                    print("Img path before:", img_path)

                    # path_and_filename = img_path.rsplit('\\', 1)  # split path to main_path+filename
                    # print(path_and_filename)
                    # path_to_file = path_and_filename[0]  # path before file
                    # filename = path_and_filename[1]  # filename
                    # os.rename(img_path, path_to_file + '\\' + rename_file(filename))
                    # img_path = path_to_file + '\\' + rename_file(filename)  # call rename function and compose img_path
        else:

            os.makedirs(plant_dir_path)  # create folder(-s)on the given path
            shutil.move(img_path, plant_dir_path)  # move img ti folder
    except Exception as exc:
        print(exc)


def rename_file(file_path):
    """This function rename file
    - Parameters:
        :file_path(str): path to file name which should be processed

    - Returns:
        :end_file_path(str): renamed file name
    """
    begin_file_path = file_path
    file_path_name = file_path.rsplit('\\', 1)  # [file_path, filename]
    file_name = file_path_name[1]  # get filename
    file_path = file_path_name[0]  # get path

    file_name_splitted = str(file_name).rsplit('.', 1)  # get massive [name, extension]
    file_name = file_name_splitted[0]  # set name
    extension = '.' + file_name_splitted[1].lower()  # set extension (for example: .png)

    if len(file_name) < 20:  # if len of filename < 20 letters
        renamed_file = file_name + '_' + ''.join(choice(ascii_letters)for i in range(4))  # add random symbols in end name
    else:
        renamed_file = ''.join(choice(ascii_letters) for i in range(10))  # generate random file name
    renamed_file += extension  # add extension to name

    end_file_path = file_path + '\\' + renamed_file  # compose finally path
    os.rename(begin_file_path, end_file_path)  # procedure renaming file

    return end_file_path


def check_file_name(file_name):
    """This function reformat file name if these is invalid(not eng letters)
    - Parameters:
        :file_name(str): file name which should be processed if such a name is already in the media folder

    - Returns:
        :file_name(str): reformatted file name
    """

    file_name_splitted = str(file_name).rsplit('.', 1)  # get massive [name, extension]
    file_name = file_name_splitted[0]  # set name
    extension = '.' + file_name_splitted[1].lower()  # set extension (for example: .png)

    if not re.fullmatch(r'[A-Za-z0-9._-]{1,35}', file_name):  # if does not match the pattern
        file_name = ''.join(choice(ascii_letters) for i in range(10))  # generate random file name
        file_name += extension  # add extension to name
    else:
        file_name += extension  # add extension to name

    return file_name


def check_filename_extension(file_name):
    """This function check forbidden extensions and return False if extension allow
    - Parameters:
        :file_name(str): file name which should be checked for possible malicious content.

    - Returns:
        :return_data(bool): bool False if file clear. Otherwise True.
    """

    return_data = False
    try:
        extension = str(file_name).split('.')[-1]  # get extension
        extension_list = ['exe', 'msi', 'bat', 'apk', 'py', 'bin', 'cmd', 'jar', 'ps1', 'msu', 'wsf', 'cgi', 'com',
                          'gadget', 'reg']  # list forbidden extensions
        if extension.lower() in extension_list:  # check
            return_data = True
    except Exception:
        print('>>> Error check_filename_extension()')

    return return_data


def delete_file(file_path):
    """This function try delete file from media
    - Parameters:
        :file_path(str): path to file which should do deleted
    """

    try:
        full_path = str(pathlib.Path(__file__).parent.absolute()).replace('\\NeuralNetwork\\apps\\neuralmain\\tools',
                                                                          '') + str(file_path).replace('/', '\\')
        os.remove(full_path)  # remove file
    except Exception:
        pass
