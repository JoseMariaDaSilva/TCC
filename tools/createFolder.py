import os
from tqdm import tqdm
from time import sleep
import shutil

def createFolder(nDivisions):
    messages = []
    paths = os.listdir(os.path.join(os.path.abspath('.'),'images'))
    partsDir = ['part_'+str(x) for x in range(1,nDivisions+1)]
    path_train = os.path.join(os.path.join(os.path.abspath('.'),'images'),paths[1])
    path_test = os.path.join(os.path.join(os.path.abspath('.'),'images'),paths[0])

    uris = [path_train,path_test]

    for paths in partsDir:
        shutil.rmtree(os.path.join(path_test,paths),ignore_errors=True)
        shutil.rmtree(os.path.join(path_train,paths),ignore_errors=True)

    for u in tqdm(uris):
        for path in partsDir:
            uri = os.path.join(u,path)
            if not os.path.exists(uri):
                os.mkdir(uri)
    
    
    if len(os.listdir(uris[0]))>nDivisions:
        for u in tqdm(uris):
            for parts in os.listdir(u):
                if not (parts in partsDir):
                    shutil.rmtree(os.path.join(u,parts),ignore_errors=True)
                    #os.rmdir(os.path.join(u,parts))
                    

    

