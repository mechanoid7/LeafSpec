""" This module makes it possible to check file extension and name, delete file

    :Date: 24-04-2020
    :Version: Beta
    :Authors:
        - Mechanoid
"""

import pathlib
import re, os
from random import choice
from string import ascii_letters


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

    if not re.fullmatch('[A-Za-z0-9_.-]', file_name):  # if does not match the pattern
        file_name = ''.join(choice(ascii_letters) for i in range(10))  # generate random file name
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
