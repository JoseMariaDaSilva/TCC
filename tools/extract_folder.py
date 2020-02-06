import os
import pandas as pd
import numpy as np

class searchCSv:
    def __init__(self,path):
        try:
            self.path = os.path.abspath(str(path))
        except FileNotFoundError as e:
            print('Arquivo ou pasta nao encontrada',e)
        
    
    def dataStructure(self,data):
        return np.array(pd.read_csv(os.path.join(self.path,data),engine='python')['2.0A'][800:]).astype('float')