from django.contrib import admin
from .models import PhotoRequest, PhotoToDatabase
# from os import subprocess
import os
import pathlib
import datetime
# Register your models here.

admin.site.register(PhotoRequest)
# admin.site.register(PhotoInDatabase)
admin.site.register(PhotoToDatabase)
# admin.site.register(PhotoAnswer)

auth_data = {
    'mechanoid': 'mechanoid',
    'user': 'user32',
    'opg_gremlin': 'iliuha'
}


def relearning():
    """Get current path and modified him, add command to relearning NeuralNet"""
    f = open(str(pathlib.Path(__file__).parent.absolute()) +'\\bin\\ReLearningSystem.ps1', 'w')

    bin_path = str(pathlib.Path(__file__).parent.absolute()) +'\\bin\\'

    msg = '# ' + str(datetime.datetime.now())
    command1 = f'python.exe {bin_path}scripts\\retrain.py --output_graph={bin_path}tf_files\\retrained_graph.pb --output_labels={bin_path}tf_files\\retrained_labels.txt --image_dir={bin_path}tf_files\\leaf_photos'
    command2 = 'Sleep -Seconds 15'

    f.write(msg + '\n')
    f.write(command1 + '\n')
    f.write(command2)
    f.close()

    # os.startfile(str(pathlib.Path(__file__).parent.absolute())+'\\bin\\ReLearningSystem.ps1')



#python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/leaf_photos
