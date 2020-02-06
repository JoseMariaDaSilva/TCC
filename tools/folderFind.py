import os
from calculate import Arms
from extract_folder import searchCSv



def folderFind():
    path = os.path.abspath('.')
    folder = list(filter(lambda x:x==('Test_motor_normal'),os.listdir(path)))[0]
    filesCsv = list(filter(lambda x:x.endswith('.CSV'),os.listdir(os.path.join(path,folder))))
    filesCsv = os.listdir(folder)
    number_files = len(filesCsv)

    structure = {}
    maxRms = {}
    for file, number in zip(filesCsv,range(number_files)):
        structure['ensaio_'+str(number)] = Arms(searchCSv(os.path.join(path,folder)).dataStructure(file)).rms()
        maxRms['ensaio_'+str(number)] = max(Arms(searchCSv(os.path.join(path,folder)).dataStructure(file)).rms())

    return structure,maxRms
