import pathlib
import datetime
import os


def delta_datetime(datetime_old_get):
    """Get str from file and find for time difference(in second)"""
    datetime_old = str(datetime_old_get).replace('#', '').replace('\n', '')  # delete '\n' and '#' from str
    datetime_now = datetime.datetime.now()  # take current datetime
    datetime_old = datetime.datetime.strptime(datetime_old, '%Y-%m-%d %H:%M:%S')  # convert str to <datetime> object
    datetime_delta = datetime_now - datetime_old  # find datetime difference and convert to seconds
    delta = datetime_delta.seconds  # get delta time in sec
    delta += datetime_delta.days*86400  # convert delta date to sec, sum(date + time)
    return delta


def retrain_sys():
    """ This function try retrain system, sys cannot retrain if  not enough time has passed """

    bin_path = str(pathlib.Path(__file__).parent.absolute()).replace('tools', '') +'bin\\'  # path to 'bin' dir
    ps1_path = bin_path +'ReLearningSystem.ps1'

    delta = 18000  # default value, if file missing. 18000sec -> 5hour
    request_delta = 17999  # min delta value(seconds) for retrain
    try:
        f = open(ps1_path, 'r')
        delta = delta_datetime(f.readline(64))  # read first line and override delta, if file available
        f.close()
    except Exception:
        print(f'>>>The file cannot be found, a new one will be created.')

    if delta > request_delta:  # if enough time has passed
        """ function create PowerShell file (.ps1)
        datetime_line - write to file current data and time
        command1 - command to retrain system
        command2 - command to sleep after doing
        """
        # print("PATH: >>>", bin_path)
        f = open(ps1_path, 'w')
        datetime_line = '#' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        command1 = f'python.exe {bin_path}scripts\\retrain.py --output_graph={bin_path}tf_files\\retrained_graph.pb --output_labels={bin_path}tf_files\\retrained_labels.txt --image_dir={bin_path}tf_files\\leaf_photos'
        command2 = 'Sleep -Seconds 300'

        f.write(datetime_line + '\n')  # write commands to file
        f.write(command1 + '\n')
        f.write(command2)
        f.close()

        print('>>> Start retrain system...')
        os.startfile(ps1_path)  # run script
        return_arg = [True]  # function return 'True' if retrain successful
    else:
        print(f'>>> Unsuccessful attempt to retrain system, '
              f'little time has passed since the last training({delta/3600:.2f} hours). '
              f'Need {request_delta/3600:.2f}+ hours.')

        return_arg = [False, (request_delta-delta)/3600]  # function return ['False', time to capabilities retrain]
                                                          # if retrain failed

    return return_arg



#python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/leaf_photos
