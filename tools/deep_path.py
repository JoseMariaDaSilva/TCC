import os
from shutil import rmtree
def deep_folder_location(path, level=1, no_deep = False, revere=False):
    current_path = os.path.abspath('.')
    if no_deep:
        deep = current_path.split("\\")[:-level:]
    else:
        deep = current_path.split('\\')
    return os.path.join('\\'.join(deep), path)


def delete_folder_exists(folder_name):
    path = deep_folder_location('motores_registrados')
    path_f = os.path.join(path, folder_name)
    rmtree(path_f, ignore_errors=True)
    
