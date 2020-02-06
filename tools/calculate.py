from converter_rms import Vrms
import numpy as np


class Arms(object):
    
    def __init__(self,data):
        self.data = list(map(lambda x: x**2,data))
        self._baseMenor = range(0,len(data))
        self._baseMaior = range(1,len(data))
        
    def trape(self,b,B,h):
        return ((b+B)*h)/2
    
    def rms(self):
        h = 1/(60*42)
        newData = []
        areaData = []
        for x,y in zip(self._baseMenor,self._baseMaior):
            newData.append(self.trape(self.data[x],self.data[y],h))

        for i in range(len(newData)):
            areaData.append(sum(newData[i:42+i]))
            
        areaData = np.array(areaData)
        
        return np.sqrt(areaData*60)
