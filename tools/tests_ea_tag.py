import os

def make_dir_a_tag(tag):
    
    root = os.path.abspath('.')
    motor = list(filter(lambda x: x=='motores_registrados', os.listdir(root)))[0]
    motor_path = os.path.join(root, motor)
    location_tag = os.path.join(motor_path, tag)
    
    try:
        if not os.path.exists(tag):
            os.makedirs(os.path.join(location_tag,'dataset'))
            os.makedirs(os.path.join(location_tag,'ensaios'))
    except:
        return "Tag registrada ja existe ou servidor offline.",0
    else:
        return "Cadastro feito com sucesso.",1

def search_destination_path(tag, destination):
    root = '\\'.join(os.path.abspath('.').split('\\')[:-1:])
    new_path = os.path.join(root, 'motores_registrados')
    dirir = os.path.join(os.path.join(new_path,tag), destination)
    return dirir