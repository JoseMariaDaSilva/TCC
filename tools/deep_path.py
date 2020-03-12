import os


def deep_folder_location(level, path, revere=False):
    current_path = os.path.abspath('.')
    deep = current_path.split("\\")[:-level:]
    return os.path.join('\\'.join(deep), path)

print(deep_folder_location(1, 'motores_registrados'))
