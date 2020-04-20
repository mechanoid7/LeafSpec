import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os


def load_training_images():
    # путь к файлам изображений для тренировки нейросети
    path_train_img = os.getcwd().split('NeuralNetwork')[0]+'NeuralNetwork_res\\training_images'
    tree = os.walk(path_train_img)  # получить дерево файлов

    folder = []  # пути к всем папкам и обьектам
    for obj in tree:
        """Если путь заканчивается на "raw" - не добавлять в массив путей"""
        if obj[0].split('\\')[-1] != 'raw':
            """Добавлять в массив только первый и последний элемент подмассовов, 
            таким образом массив будет содержать только путь к изображениям и подмассив самих изображений"""
            folder.append([obj[0], obj[-1]])

    type_and_files = []
    for obj in folder:
        """Заполняем двумерный массив 'type_and_files'. 
        Первый элемент - вид растения, второй - массив с изображениями"""
        type_and_files.append([obj[0].split('\\')[-1], obj[-1]])
        # print(obj[-1].shape)


    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    print(train_images.shape)

    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)





# load_training_images()


# hello = tf.constant('hello')
# sess = tf.compat.v1.Session()
# print(sess.run(hello))


