import os

def make_dir_a_tag(tag):
    
    root = os.path.abspath('.')
    print(root)
    print(os.listdir(root))
    motor = list(filter(lambda x: x=='motores_registrados', os.listdir(root)))[0]
    motor_path = os.path.join(root, motor)
    location_tag = os.path.join(motor_path, tag)
    
    
    if not os.path.exists(tag):
        os.makedirs(os.path.join(location_tag,'dataset'))
        