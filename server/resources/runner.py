#!/usr/bin/python
# -*- coding:utf-8 -*-


import resources.ADS1256 as ADS1256
import RPi.GPIO as GPIO
import threading
from datetime import datetime



def run(instance):
    data = []
    th1 = threading.currentThread()
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    
    while getattr(th1, "do_run", True):
        data.append(round(ADC.ADS1256_GetSingleChannel(0)*5.0/0x7fffff,3))
    instance.put(data)
    GPIO.cleanup()



 
    
    
